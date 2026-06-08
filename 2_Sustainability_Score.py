import streamlit as st
from model import predict_score
from ui import apply_background
apply_background()

st.set_page_config(page_title="EcoHabit🌱", layout="wide")

if "transport" not in st.session_state:
    st.warning("Please fill lifestyle questions in Dashboard first.")
    st.stop()

st.title("🌍 Sustainability Score Calculator")

score = predict_score(
    st.session_state.transport,
    st.session_state.recycle,
    st.session_state.plastic,
    st.session_state.meat
)

score = round(score,2)

st.metric("Your Sustainability Score",f"{score}/100")
st.progress(score/100)

if score < 40:
    level = "🌱 Beginner"
elif score < 70:
    level = "🌿 Eco Learner"
elif score < 90:
    level = "🌳 Green Champion"
else:
    level = "🌍 Climate Hero"

st.success(f"Eco Level: {level}")