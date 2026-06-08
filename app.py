import streamlit as st
import sqlite3
from ui import apply_background
apply_background()

st.set_page_config(page_title="EcoHabit🌱", layout="wide")

# -----------------------------
# DATABASE
# -----------------------------

conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users(
username TEXT PRIMARY KEY,
password TEXT,
tokens INTEGER,
streak INTEGER
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS tasks(
username TEXT,
task TEXT,
completed INTEGER
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS token_history(
username TEXT,
date TEXT,
tokens INTEGER
)
""")

conn.commit()

# -----------------------------
# SESSION STATE
# -----------------------------

if "user" not in st.session_state:
    st.session_state.user = None

if "tokens" not in st.session_state:
    st.session_state.tokens = 0

if "streak" not in st.session_state:
    st.session_state.streak = 1

# -----------------------------
# LOGIN / SIGNUP
# -----------------------------

if st.session_state.user is None:

    menu = ["Login","Signup"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Signup":

        st.title("Create Account")

        username = st.text_input("Username")
        password = st.text_input("Password",type="password")

        if st.button("Signup"):

            try:
                c.execute(
                "INSERT INTO users(username,password,tokens,streak) VALUES(?,?,0,1)",
                (username,password)
                )

                conn.commit()
                st.success("Account created!")

            except:
                st.error("Username already exists")


    if choice == "Login":

        st.title("Login")

        username = st.text_input("Username")
        password = st.text_input("Password",type="password")

        if st.button("Login"):

            c.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username,password)
            )

            user = c.fetchone()

            if user:

                st.session_state.user = username
                st.session_state.tokens = user[2]
                st.session_state.streak = user[3]

                st.success("Login successful")
                st.rerun()

# -----------------------------
# AFTER LOGIN
# -----------------------------

if st.session_state.user:

    if st.sidebar.button("Logout"):

        st.session_state.user = None
        st.session_state.tokens = 0
        st.session_state.streak = 1

        st.rerun()

    st.sidebar.success(f"Logged in as {st.session_state.user}")