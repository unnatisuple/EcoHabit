import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()


# -----------------------------
# CREATE TABLES
# -----------------------------

def create_tables():

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT,
        tokens INTEGER DEFAULT 0,
        streak INTEGER DEFAULT 1
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        username TEXT,
        task TEXT,
        completed INTEGER
    )
    """)

    conn.commit()


# -----------------------------
# ADD USER (Signup)
# -----------------------------

def add_user(username,password):

    try:

        c.execute(
        "INSERT INTO users(username,password) VALUES (?,?)",
        (username,password)
        )

        conn.commit()

        return True

    except:

        return False


# -----------------------------
# LOGIN USER
# -----------------------------

def login_user(username,password):

    c.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username,password)
    )

    return c.fetchone()


# -----------------------------
# UPDATE TOKENS
# -----------------------------

def update_tokens(username,tokens):

    c.execute(
    "UPDATE users SET tokens=? WHERE username=?",
    (tokens,username)
    )

    conn.commit()


# -----------------------------
# SAVE TASKS
# -----------------------------

def save_task(username,task,completed):

    c.execute(
    "INSERT INTO tasks VALUES (?,?,?)",
    (username,task,completed)
    )

    conn.commit()