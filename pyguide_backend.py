from flask import Flask, request, render_template, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from datetime import datetime 
import bcrypt
from questions_data import questions
import io, sys


app = Flask(__name__)
app.secret_key = "123"  

# Setting up database
db_cred = {
    'user': 'root',
    'pass': '',
    'host': 'localhost',
    'name': 'pyguide' 
}

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://\
{db_cred['user']}:{db_cred['pass']}@{db_cred['host']}/\
{db_cred['name']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
connection = engine.connect()


# Welcome Page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Get user from the database
    with db.engine.connect().execution_options(autocommit=True) as connection: # To get updated data from database
        query = text("SELECT * FROM User WHERE username = :username")
        result = connection.execute(query, {'username': username}).fetchone()

    if not result:
        flash('Invalid username or password', 'error')
        return redirect(url_for('welcome'))

    hashed_password = result[4]
    # Password checking
    try:
        if result[4] == password: 
            flash(f'Welcome back, {username}!', 'success')
            session['user_id'] = result[0]
            session['username'] = result[1]
        
            return redirect(url_for('display_lessons'))
        elif bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            flash(f'Welcome back, {username}!', 'success')
            session['user_id'] = result[0]
            session['username'] = result[1]
       
            return redirect(url_for('display_lessons'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('welcome'))
    except:
        flash('Invalid username or password', 'error')
        return redirect(url_for('welcome'))


# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['fullname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        age = request.form['age']

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        try:
            with db.engine.connect() as connection:
                transaction = connection.begin()

                # Check if the username or email already exists
                check_query = text("""SELECT * FROM User WHERE Username = :username OR Email = :email""")
                result = connection.execute(check_query, {'username': username, 'email': email}).fetchone()

                # User already exists
                if result:
                    flash('Username or Email already exists', 'error')
                    transaction.rollback()  
                    return redirect(url_for('welcome'))

                # Call the signUp stored procedure
                sign_up_query = text(""" CALL signUp(:full_name, :email, :username, :password, :age)""")
                connection.execute(sign_up_query, {'full_name': full_name,
                                                    'email': email,
                                                    'username': username,
                                                    'password': hashed_password,
                                                    'age': age})
                # Saving Changes to the database
                transaction.commit()
                flash('User registered successfully!', 'success')
                return redirect(url_for('welcome'))
        except Exception as e:
            transaction.rollback()
            flash(f'An error occurred while registering: {e}', 'error')
            return redirect(url_for('welcome'))

    return render_template('register.html')



# Displaying lessons for the user
@app.route('/lessons')
def display_lessons():
    if 'user_id' not in session:
        flash('Please log in first', 'error')
        return redirect(url_for('welcome'))

    user_id = int(session['user_id'])
    with db.engine.connect() as connection:
        
        # Load user age + recent lesson
        user_row = connection.execute(
            text("SELECT age, recent_lesson, completed_lessons FROM User WHERE user_ID = :uid"),
            {'uid': user_id}
        ).fetchone()

        age = user_row[0]
        recent_lesson = user_row[1]
        completed_raw = user_row[2]
        lessons_level2 = []   
        lessons_level3 = []   

        if completed_raw:
            completed_lessons = list(map(int, completed_raw.split(',')))
        else:
            completed_lessons = []

        # Determine level
        if age <= 12:
            level = 1
        elif age <= 15:
            level = 2
        else:
            level = 3

        lessons_rows = connection.execute(
            text("SELECT lesson_ID, name, level, next_lesson FROM Lesson WHERE level = :lvl ORDER BY lesson_ID"),
            {'lvl': level}
        ).fetchall()

        lessons = []
        for i, row in enumerate(lessons_rows):
            lesson_id = row[0]
            name = row[1]

            is_completed = lesson_id in completed_lessons
            is_unlocked = False

            if i == 0:
                is_unlocked = True

            if i > 0:
                prev_lesson_id = lessons_rows[i-1][0]
                if prev_lesson_id in completed_lessons:
                    is_unlocked = True

            if 5 in completed_lessons and 6 <= lesson_id <= 10:
                is_unlocked = True

            lessons.append({
                "id": lesson_id,
                "name": name,
                "completed": is_completed,
                "unlocked": is_unlocked})


        if 5 in completed_lessons:
            level2_rows = connection.execute(
                text("SELECT lesson_ID, name, level, next_lesson FROM Lesson WHERE level = 2 ORDER BY lesson_ID")
            ).fetchall()

            for i, row in enumerate(level2_rows):
                lesson_id_2 = row[0]
                name_2 = row[1]

                is_completed_2 = lesson_id_2 in completed_lessons
                is_unlocked_2 = False

                # unlock all lessons up to and including String Methods (lesson_ID 11)
                if lesson_id_2 <= 11:
                    is_unlocked_2 = True
                else:
                    if i > 0:
                        prev_id_2 = level2_rows[i-1][0]
                        if prev_id_2 in completed_lessons:
                            is_unlocked_2 = True

                lessons_level2.append({
                    "id": lesson_id_2,
                    "name": name_2,
                    "completed": is_completed_2,
                    "unlocked": is_unlocked_2
                })


        if 14 in completed_lessons:
            level3_rows = connection.execute(
                text("SELECT lesson_ID, name, level, next_lesson FROM Lesson WHERE level = 3 ORDER BY lesson_ID")
            ).fetchall()

            for i, row in enumerate(level3_rows):
                lesson_id_3 = row[0]
                name_3 = row[1]

                is_completed_3 = lesson_id_3 in completed_lessons
                is_unlocked_3 = False

                # unlock all lessons up to and including Files_Exceptions (lesson_ID 24)
                if lesson_id_3 <= 24:
                    is_unlocked_3 = True
                else:
                    if i > 0:
                        prev_id_3 = level3_rows[i-1][0]
                        if prev_id_3 in completed_lessons:
                            is_unlocked_3 = True

                lessons_level3.append({
                    "id": lesson_id_3,
                    "name": name_3,
                    "completed": is_completed_3,
                    "unlocked": is_unlocked_3
                })


        # If user has no recent lesson yet, assign first lesson
        if not recent_lesson:
            recent_lesson = lessons[0]["id"] 

        display_recent_lesson = None

        if 1 <= recent_lesson <= 5:
            display_recent_lesson = recent_lesson         

        elif 6 <= recent_lesson <= 14:
            display_recent_lesson = recent_lesson - 5     

        elif 15 <= recent_lesson <= 26:
            display_recent_lesson = recent_lesson - 14    

        completed_count = len(completed_lessons)
        total_lessons = len(lessons_rows)

        recent_lesson_name = connection.execute(
            text("SELECT name FROM Lesson WHERE lesson_ID = :lid"),
            {'lid': recent_lesson}
        ).fetchone()[0]

        
        all_lessons_ordered = connection.execute(
            text("SELECT lesson_ID, level FROM Lesson ORDER BY lesson_ID")).fetchall()

        # Separate by level
        level1_all = [l[0] for l in all_lessons_ordered if l[1] == 1]
        level2_all = [l[0] for l in all_lessons_ordered if l[1] == 2]
        level3_all = [l[0] for l in all_lessons_ordered if l[1] == 3]

        # Completed per level
        completed_level1 = sum(l in completed_lessons for l in level1_all)
        completed_level2 = sum(l in completed_lessons for l in level2_all)
        completed_level3 = sum(l in completed_lessons for l in level3_all)


    return render_template(
        'lessons.html',
        recent_lesson=display_recent_lesson,
        recent_lesson_name=recent_lesson_name,
        lessons=lessons,
        level=level,
        completed_count=completed_count,
        total_lessons=total_lessons,
        lessons_level2=lessons_level2,
        lessons_level3=lessons_level3,
        completed_level1=completed_level1,
        completed_level2=completed_level2,
        completed_level3=completed_level3,
        total_level1=len(level1_all),
        total_level2=len(level2_all),
        total_level3=len(level3_all)  
    )


@app.route("/lesson/<int:lesson_id>")
def lesson_detail(lesson_id):
    try:
        return render_template(f"lesson_pages/lesson{lesson_id}.html")
    except:
        return "Lesson not found", 404



def run_user_code(user_code, test_expression, setup_code=""):

    safe_globals = {
    "__builtins__": {
        "print": print,
        "range": range,
        "len": len,
        "int": int,
        "str": str,
        "float": float,
        "bool": bool,
        "all": all}}

    safe_locals = {}

    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()

    try:
        full_code = setup_code + "\n" + user_code

        exec(full_code, safe_globals, safe_locals)

        sys.stdout = old_stdout
        __output__ = buffer.getvalue()
        safe_globals["__output__"] = __output__
        result = eval(test_expression, safe_globals, safe_locals)

        return {
            "correct": bool(result),
            "error": None}

    except Exception as e:
        sys.stdout = old_stdout
        return {
            "correct": False,
            "error": f"{type(e).__name__}: {e}"}


    
@app.route("/lesson/<int:lesson_id>/question/<int:qnum>", methods=["GET", "POST"])
def lesson_question(lesson_id, qnum):
    lesson_questions = questions.get(lesson_id)

    if not lesson_questions:
        return "Lesson not found", 404

    # If user finished all questions
    if qnum > len(lesson_questions):
        user_id = session.get('user_id')

        if user_id:
            with db.engine.begin() as connection:

                row = connection.execute(
                    text("SELECT completed_lessons FROM User WHERE user_ID = :uid"),
                    {'uid': user_id}).fetchone()

                if row and row[0]:
                    completed = [c for c in row[0].split(',') if c.strip() != ""]
                else:
                    completed = []

                if str(lesson_id) not in completed:
                    completed.append(str(lesson_id))

                updated_val = ",".join(completed)

                connection.execute(
                    text("""
                        UPDATE User SET completed_lessons = :val
                        WHERE user_ID = :uid
                    """),
                    {'val': updated_val, 'uid': user_id})

                points_row = connection.execute(
                    text("SELECT points FROM Lesson WHERE lesson_ID = :lid"),
                    {'lid': lesson_id}).fetchone()

                lesson_points = points_row[0] if points_row else 0

                connection.execute(
                    text("""
                        UPDATE User SET score = COALESCE(score, 0) + :pts
                        WHERE user_ID = :uid
                    """),
                    {'pts': lesson_points, 'uid': user_id})

                new_recent = lesson_id
                if lesson_id == 5:
                    new_recent = 11
                elif lesson_id == 14:
                    new_recent = 24


                connection.execute(
                    text("""
                        UPDATE User SET recent_lesson = :lid
                        WHERE user_ID = :uid
                    """),
                    {'lid': new_recent, 'uid': user_id})


                if lesson_id == 5:
                    return render_template("level1_complete.html")
                elif lesson_id == 14:
                    return render_template("level2_complete.html")
                elif lesson_id == 26:
                    return render_template("level3_complete.html")
                else:
                    if 1 <= lesson_id <= 5:
                        display_num = lesson_id                      
                    elif 6 <= lesson_id <= 14:
                        display_num = lesson_id - 5                  
                    elif 15 <= lesson_id <= 26:
                        display_num = lesson_id - 14                
                    else:
                        display_num = lesson_id

                    return render_template("lesson_complete.html", lesson_id=lesson_id, display_num=display_num)



    question = next((q for q in lesson_questions if q["qnum"] == qnum), None)
    if not question:
        return "Question not found", 404

    user_answer = None
    is_correct = None
    error_message = None  

    if request.method == "POST":
        user_answer = request.form.get("answer")

        if question["type"] == "mcq":
            is_correct = (user_answer == question["correct"])

        elif question["type"] == "code":
            result = run_user_code(
                user_answer,
                question["test"],
                question.get("setup", "")
            )
            is_correct = result["correct"]
            error_message = result["error"]

    return render_template(
        "question_template.html",
        question=question,
        lesson_id=lesson_id,
        qnum=qnum,
        is_correct=is_correct,
        user_answer=user_answer,
        error_message=error_message  )


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    try:
        user_id = int(session['user_id'])
    except:
        flash("Please sign in to view your profile.", "error")
        return redirect(url_for('welcome'))

    try:
        with db.engine.connect() as connection:
            transaction = connection.begin()

            if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
                fullname = request.form['fullname']
                email = request.form['email']

                hashed_password = None
                if password:
                    hashed_password = bcrypt.hashpw(
                        password.encode('utf-8'),
                        bcrypt.gensalt()
                    ).decode('utf-8')

                try:
                    if hashed_password:
                        query = text("""
                            UPDATE User 
                            SET name = :fullname, email = :email,
                                username = :username, password = :password 
                            WHERE user_ID = :user_id
                        """)
                        connection.execute(query, {
                            'fullname': fullname,
                            'email': email,
                            'username': username,
                            'password': hashed_password,
                            'user_id': user_id
                        })
                    else:
                        query = text("""
                            UPDATE User 
                            SET name = :fullname, email = :email,
                                username = :username
                            WHERE user_ID = :user_id
                        """)
                        connection.execute(query, {
                            'fullname': fullname,
                            'email': email,
                            'username': username,
                            'user_id': user_id
                        })

                    transaction.commit()
                    flash("Profile updated successfully.", "success")

                except Exception as e:
                    transaction.rollback()
                    flash(f"An error occurred while updating the profile: {e}", "error")


            query = text("""
                SELECT user_ID, name, email, username, score, completed_lessons, avatar
                FROM User
                WHERE user_ID = :user_id
            """)
            result = connection.execute(query, {'user_id': user_id}).fetchone()

            if not result:
                flash("User not found.", "error")
                return redirect(url_for('welcome'))

            user_details = {
                'User_ID': result[0],
                'FullName': result[1],
                'Email': result[2],
                'Username': result[3],
                'Score': result[4] or 0,
                'Avatar': result[6]
            }

            completed_raw = result[5] or ""
            completed_lessons = [int(x) for x in completed_raw.split(',') if x.strip()]


            LEVEL1_TOTAL = 5

            badges = compute_badges(
                score=user_details['Score'],
                completed_lessons=completed_lessons,
                level1_total=LEVEL1_TOTAL
            )

            title = get_title(user_details['Score'])


            return render_template(
                'profile.html',
                user=user_details,
                badges=badges,
                title=title)

    except Exception as e:
        flash(f"An error occurred: {e}", "error")
        return redirect(url_for('welcome'))


@app.route('/leaderboard')
def leaderboard():
    if 'user_id' not in session:
        flash("Please log in first.", "error")
        return redirect(url_for('welcome'))

    user_id = session['user_id']

    with db.engine.connect() as connection:
        users = connection.execute(
        text("""
            SELECT 
                user_ID AS user_id,
                username,
                COALESCE(score, 0) AS score,
                avatar
            FROM User
            ORDER BY score DESC
            LIMIT 20""")).mappings().all()


    return render_template(
        "leaderboard.html",
        users=users,
        current_user_id=session["user_id"]) 
    

@app.route('/logout')
def logout():
    session.clear()  
    flash("You have been logged out.", "info")
    return redirect(url_for('welcome'))


# Gamification Elements

AVATARS = [
    {"img": "/static/avatars/cat.png", "min_score": 0},
    {"img": "/static/avatars/dog.png", "min_score": 20},
    {"img": "/static/avatars/ninja.png", "min_score": 40},
    {"img": "/static/avatars/wizard.png", "min_score": 70},
    {"img": "/static/avatars/dragon.png", "min_score": 120},
    {"img": "/static/avatars/kuma1.png", "min_score": 500},
    {"img": "/static/avatars/unicorn.png", "min_score": 1000},
    {"img": "/static/avatars/castle.png", "min_score": 3000}

]

@app.route("/avatars")
def avatar_select():
    if "user_id" not in session:
        return redirect("/")

    user_id = session["user_id"]

    with db.engine.connect() as connection:
        row = connection.execute(
        text("""
            SELECT 
                COALESCE(score, 0) AS score,
                COALESCE(avatar, '/static/avatars/python.png') AS avatar
            FROM User
            WHERE user_ID = :uid
        """),
        {"uid": user_id}
    ).mappings().one()


    return render_template(
        "avatar_select.html",
        avatars=AVATARS,
        user_score=row["score"],
        session_avatar=row["avatar"])



@app.route("/select_avatar", methods=["POST"])
def select_avatar():
    if "user_id" not in session:
        return redirect("/")

    chosen = request.form.get("avatar")

    if chosen not in [a["img"] for a in AVATARS]:
        flash("Invalid avatar selection.", "error")
        return redirect(url_for("avatar_select"))

    user_id = session["user_id"]

    with db.engine.begin() as connection:
        connection.execute(
            text("""
                UPDATE User
                SET avatar = :avatar
                WHERE user_ID = :uid
            """),
            {"avatar": chosen, "uid": user_id}
        )

    flash("New avatar selected!", "success")
    return redirect(url_for("profile"))




BADGES = [
    {
        "id": "first_lesson",
        "name": "Starter Coder",
        "icon": "🌱",
        "desc": "Completed your first lesson."
    },
    {
        "id": "level1_master",
        "name": "Level 1 Master",
        "icon": "🏆",
        "desc": "Completed all Level 1 lessons."
    },
    {
        "id": "score_50",
        "name": "On Fire",
        "icon": "🔥",
        "desc": "Reached 50 points."
    },
    {
        "id": "score_100",
        "name": "Python Pro",
        "icon": "🐍",
        "desc": "Reached 100 points."
    },
    {
        "id": "score_250",
        "name": "Code Warrior",
        "icon": "⚔️",
        "desc": "Reached 250 points."
    },
    {
        "id": "score_500",
        "name": "Algorithm Adept",
        "icon": "🧠",
        "desc": "Reached 500 points."
    },
    {
        "id": "score_1000",
        "name": "Code Champion",
        "icon": "🥇",
        "desc": "Reached 1,000 points."
    },
    {
        "id": "score_2000",
        "name": "Legendary Engineer",
        "icon": "🏅",
        "desc": "Reached 2,000 points."
    },
    {
        "id": "score_4000",
        "name": "Grandmaster Coder",
        "icon": "👑",
        "desc": "Reached 4,000 points."
    },
]


def get_title(score: int) -> str:
    if score < 20:
        return "New Explorer"
    elif score < 50:
        return "Rising Coder"
    elif score < 100:
        return "Python Knight"
    elif score < 250:
        return "Code Warrior"
    elif score < 500:
        return "Algorithm Adept"
    elif score < 1000:
        return "Code Champion"
    elif score < 2000:
        return "Legendary Engineer"
    else:
        return "Grandmaster Coder"


def compute_badges(score: int, completed_lessons: list, level1_total: int) -> list:
    earned = []

    if len(completed_lessons) >= 1:
        earned.append(BADGES[0])

    if level1_total > 0 and len([l for l in completed_lessons if l <= level1_total]) >= level1_total:
        earned.append(BADGES[1])

    if score >= 50:
        earned.append(BADGES[2])
    if score >= 100:
        earned.append(BADGES[3])
    if score >= 250:
        earned.append(BADGES[4])
    if score >= 500:
        earned.append(BADGES[5])
    if score >= 1000:
        earned.append(BADGES[6])
    if score >= 2000:
        earned.append(BADGES[7])
    if score >= 4000:
        earned.append(BADGES[8])

    return earned


if __name__ == '__main__':
    app.run(debug=True)
