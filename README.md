# PyGuide
> **Senior Design Project** — An interactive Python learning web application

PyGuide helps students develop programming skills through structured lessons, code exercises, scoring, badges, and avatar progression. Built with a Flask backend and MySQL database, it provides a beginner-friendly interface while giving instructors easy access to monitor user progress.

---

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Database Setup](#database-setup)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Usage](#usage)
- [Demo Account](#demo-account)

---

## Overview

PyGuide is designed for beginner programmers and their instructors. Students can:
- Work through structured Python lessons
- Submit code exercises and receive scores
- Earn badges and unlock new avatars as they progress
- Track their progress via a personal profile page

Instructors can monitor all user data at any time through phpMyAdmin.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python / Flask |
| Database | MySQL (via XAMPP) |
| DB Management | phpMyAdmin |
| ORM / DB Driver | SQLAlchemy, PyMySQL |
| Auth | bcrypt |

---

## Prerequisites

Install the following before running PyGuide:

### 1. XAMPP
Provides the MySQL database and phpMyAdmin interface.

🔗 [Download XAMPP](https://www.apachefriends.org/index.html)

Choose the version for your OS (macOS, Windows, or Linux).

### 2. Python 3.10+

🔗 [Download Python](https://www.python.org/downloads/)

### 3. Git *(optional)*
Only needed if you want to clone the repo via command line.

🔗 [Download Git](https://git-scm.com/downloads)

Otherwise, download the project as a ZIP from GitHub.

---

## Database Setup

1. Open XAMPP and start both services:
   - **MySQL Database**
   - **Apache Web Server**

2. Navigate to phpMyAdmin in your browser:
   ```
   http://localhost/phpmyadmin
   ```

3. Create a new database named:
   ```
   pyguide
   ```

4. Import the provided SQL file (`pyguide.sql`) from this repository.
   - This will automatically create all required tables (e.g., `User`, `Lesson`) and insert the demo admin account.

---

## Installation

**Option A — Download ZIP:**
1. Click the green **Code** button on the GitHub repository page.
2. Select **Download ZIP**.
3. Extract the ZIP to your computer.
4. Open the folder in VS Code or your preferred editor.

**Option B — Clone via Git:**
```bash
git clone <repository-url>
cd pyguide
```

**Install Python dependencies:**
```bash
pip install flask sqlalchemy pymysql bcrypt
```

---

## Running the App

Make sure XAMPP is running with MySQL and Apache active, then start the backend:

```bash
python pyguide_backend.py
```

You should see output like:
```
* Running on http://127.0.0.1:5000/
```

Open your browser and go to:
```
http://127.0.0.1:5000/
```

---

## Usage

Once the app is open:

- **Log in** with the demo admin account or **register** a new user.
- New accounts start at level 1 with beginner avatars.
- Complete lessons to earn points, badges, and unlock new avatars.
- The **profile page** displays your score, title, badges, and current avatar.
- Lesson progress is saved to MySQL so users can pick up where they left off.
- Instructors can verify user data anytime via phpMyAdmin (`User` and `Lesson` tables).

---

## Demo Account

A fully unlocked admin account is included for demonstration and grading:

| Field | Value |
|---|---|
| Username | `Mari` |
| Password | `123` |

This account has full progress unlocked and showcases all features of the application.
