import streamlit as st
import sqlite3
import pandas as pd
from ui import apply_background
apply_background()

st.set_page_config(page_title="EcoHabit🌱", layout="wide")

conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

st.title("📊 Eco Progress Analytics")

c.execute(
"SELECT date,tokens FROM token_history WHERE username=?",
(st.session_state.user,)
)

data = c.fetchall()

if data:

    df = pd.DataFrame(data,columns=["Date","Tokens"])

    df["Date"] = pd.to_datetime(df["Date"])

    df = df.groupby("Date").sum()

    st.subheader("Your Eco Token Progress")

    st.line_chart(df)

else:

    st.info("Complete tasks to generate analytics data.")