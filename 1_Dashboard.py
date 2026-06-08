import streamlit as st
import sqlite3
from model import predict_task
from datetime import date
from ui import apply_background
apply_background()

st.set_page_config(page_title="EcoHabit🌱", layout="wide")

if "user" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "task_status" not in st.session_state:
    st.session_state.task_status = {}

st.title("🌱 EcoHabit Dashboard")

col1,col2 = st.columns(2)

col1.metric("🌱 Tokens", st.session_state.tokens)
col2.metric("🔥 Streak", st.session_state.streak)

st.divider()

# -----------------------------
# LIFESTYLE INPUT
# -----------------------------

st.header("Lifestyle Questions")

transport = st.selectbox(
"Transport",
["Car","Public Transport","Walk/Cycle"]
)

recycle = st.selectbox(
"Recycle Waste",
["Yes","No"]
)

plastic = st.selectbox(
"Reusable Bottles",
["Yes","No"]
)

meat = st.selectbox(
"Meat Consumption",
["Daily","Few times","Rarely","No"]
)

st.session_state.transport = transport
st.session_state.recycle = recycle
st.session_state.plastic = plastic
st.session_state.meat = meat

# -----------------------------
# GENERATE TASKS
# -----------------------------

if st.button("Generate My Eco Tasks"):

    tasks = []

    for i in range(5):

        task = predict_task(
            transport,
            recycle,
            plastic,
            meat
        )

        tasks.append(task)

    tasks = list(set(tasks))

    st.session_state.tasks = tasks
    st.session_state.task_status = {t: False for t in tasks}

# -----------------------------
# DISPLAY TASKS
# -----------------------------

if st.session_state.tasks:

    st.subheader("🌱 Your Daily Eco Challenges")

    for task in st.session_state.tasks:

        st.write(task)

        uploaded_file = st.file_uploader(
            f"Upload proof for: {task}",
            type=["jpg","png","jpeg"],
            key=f"upload_{task}"
        )

        if uploaded_file:

            st.image(uploaded_file)

            if st.button(f"Claim reward for {task}", key=f"reward_{task}"):

                reward = 10
                st.session_state.tokens += reward

                c.execute(
                "UPDATE users SET tokens=? WHERE username=?",
                (st.session_state.tokens, st.session_state.user)
                )

                conn.commit()

                st.success(f"Task verified! {reward} tokens awarded 🌱")

# -----------------------------
# CLAIM REWARD
# -----------------------------

if st.button("Claim Reward"):

    completed = sum(st.session_state.task_status.values())

    if completed == 0:

        st.warning("Complete at least one task")

    else:

        reward = completed * 10

        st.session_state.tokens += reward
        st.session_state.streak += 1

        for task, status in st.session_state.task_status.items():

            c.execute(
                "INSERT INTO tasks VALUES(?,?,?)",
                (st.session_state.user, task, int(status))
            )

        # update user stats
        c.execute(
            "UPDATE users SET tokens=?,streak=? WHERE username=?",
            (
                st.session_state.tokens,
                st.session_state.streak,
                st.session_state.user
            )
        )

        # store token history for analytics
        today = date.today()

        c.execute(
            "INSERT INTO token_history VALUES(?,?,?)",
            (st.session_state.user, str(today), reward)
        )

        conn.commit()

        st.success(f"You earned {reward} tokens!")