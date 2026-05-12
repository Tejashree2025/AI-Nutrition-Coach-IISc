
# =========================
# FILE: database.py

# =========================

import sqlite3
import json

DB_NAME = "nutrition_app.db"

# =========================
# CONNECTION
# =========================

def get_connection():

    return sqlite3.connect(
        DB_NAME,
        check_same_thread=False
    )

# =========================
# CREATE TABLES
# =========================

def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    # =========================
    # USERS
    # =========================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        password TEXT,

        name TEXT,

        age INTEGER,

        weight REAL,

        height REAL,

        gender TEXT,

        goal TEXT,

        diet_type TEXT,

        activity_level TEXT
    )

    """)

    # =========================
    # MEAL HISTORY
    # =========================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS meal_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        meal TEXT,

        nutrition TEXT,

        glucose TEXT
    )

    """)

    conn.commit()

    conn.close()

# =========================
# REGISTER USER
# =========================

def register_user(
    username,
    password,
    name,
    age,
    weight,
    height,
    gender,
    goal,
    diet_type,
    activity_level
):

    try:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO users (

            username,
            password,
            name,
            age,
            weight,
            height,
            gender,
            goal,
            diet_type,
            activity_level

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

        """, (

            username,
            password,
            name,
            age,
            weight,
            height,
            gender,
            goal,
            diet_type,
            activity_level
        ))

        conn.commit()

        conn.close()

        return True

    except Exception as e:

        print(e)

        return False

# =========================
# LOGIN USER
# =========================

def login_user(
    username,
    password
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT * FROM users

    WHERE username=? AND password=?

    """, (

        username,
        password
    ))

    user = cursor.fetchone()

    conn.close()

    return user

# =========================
# GET USER PROFILE
# =========================

def get_user_profile(
    username
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        username,
        name,
        age,
        weight,
        height,
        gender,
        goal,
        diet_type,
        activity_level

    FROM users

    WHERE username=?

    """, (username,))

    row = cursor.fetchone()

    conn.close()

    if row is None:

        return None

    return {

        "username": row[0],
        "name": row[1],
        "age": row[2],
        "weight": row[3],
        "height": row[4],
        "gender": row[5],
        "goal": row[6],
        "diet_type": row[7],
        "activity_level": row[8]
    }

# =========================
# SAVE MEAL HISTORY
# =========================

def save_meal_history(
    username,
    meal,
    nutrition,
    glucose
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO meal_history (

        username,
        meal,
        nutrition,
        glucose

    )

    VALUES (?, ?, ?, ?)

    """, (

        username,
        meal,
        json.dumps(nutrition),
        json.dumps(glucose)
    ))

    conn.commit()

    conn.close()

# =========================
# GET MEAL HISTORY
# =========================

def get_meal_history(
    username
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT meal, nutrition, glucose

    FROM meal_history

    WHERE username=?

    ORDER BY id DESC

    """, (username,))

    rows = cursor.fetchall()

    conn.close()

    history = []

    for row in rows:

        history.append({

            "meal": row[0],

            "nutrition": json.loads(
                row[1]
            ),

            "glucose": json.loads(
                row[2]
            )
        })

    return history

