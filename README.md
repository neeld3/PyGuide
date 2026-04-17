PyGuide - Senior Design Project
PyGuide is an interactive Python-learning web application designed to help students develop programming skills through structured lessons, code exercises, scoring, badges, and avatar progression. The system provides a friendly interface for beginners while also giving instructors an easy way to monitor user progress through a MySQL database. This project uses a Flask backend, a MySQL database hosted locally through XAMPP, and a clean web interface for interacting with lessons, profiles, and user data.

To make the project easy to run on any machine, the database is provided as an SQL file. When instructors or reviewers import this file into phpMyAdmin using XAMPP, the system automatically creates the necessary tables and inserts a sample admin account. Once the database is imported, running the backend Python file will start the entire application on a local server.

Downloading Required Software
Before running the PyGuide application, the following tools must be installed:

1. XAMPP (for MySQL + phpMyAdmin)
XAMPP provides the MySQL database and the phpMyAdmin interface used by this project.
Download it here:
🔗 https://www.apachefriends.org/index.html

Choose the version for macOS, Windows, or Linux, depending on your system.

2. Python
Ensure Python 3.10 or newer is installed on your computer.
Download it here:
🔗 https://www.python.org/downloads/

3. Git (optional, for cloning the repository)
If you want to download the project directly through Git:
🔗 https://git-scm.com/downloads

Otherwise, you can download the project as a ZIP file from GitHub.

Setting Up the Database (XAMPP + phpMyAdmin)
After installing XAMPP, open the application and start the following services:

MySQL Database
Apache Web Server
Once the servers are running, open your web browser and go to:

http://localhost/phpmyadmin

This will open phpMyAdmin, which allows you to manage MySQL databases visually.

Inside phpMyAdmin, create a new database named:

pyguide

Next, import the provided SQL file included in this repository (named pyguide.sql). This file automatically creates the necessary tables — such as User and Lesson — and inserts a main test account used for demonstration and grading.

Admin account included:

Username: Mari
Password: 123
This account has full progress unlocked and can be used to showcase all features.

Downloading the Project Files
Download as ZIP
Go to the GitHub repository page.
Click the green "Code" button.
Select "Download ZIP".
Extract the ZIP file to your computer.
Open the folder in VS Code or any preferred development editor.

Installing Python Dependencies

Install required Python packages:

pip install flask sqlalchemy pymysql bcrypt

Running the Application

The entire system is controlled by the backend Python file.

Inside the project directory, run:

python pyguide_backend.py

If everything is set up correctly, the terminal will display something like:

Running on http://127.0.0.1:5000/
Copy this address into your web browser:

http://127.0.0.1:5000/

This will launch the PyGuide interface, allowing you to register new users, log in, complete lessons, change avatars, and view achievements and scoring.

How to Use the Application

Once the site is open, you may log in using the admin account (Mari / 123) or create a new user through the registration page. New accounts start at level one with beginner avatars and gradually unlock new avatars and badges as they progress through lessons. The profile page shows a user’s score, title, badges earned, and current avatar. The lesson system stores progress in the MySQL database, allowing users to pick up where they left off.

The instructor can verify user data at any time through phpMyAdmin by opening the User and Lesson tables.
