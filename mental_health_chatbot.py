import streamlit as st
import ollama
import base64
import os
import traceback

st.set_page_config(page_title="Mental Health Chatbot")

def get_base64(background):
    try:
        with open(background, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

bin_str = get_base64("background.png")

css = """
        <style>
            .stApp, .main{
            background-position: center;
            background-repeat:no-repeat;
            }
        </style>
        """

if bin_str:
    css = f"""
        <style>
            .stApp, .main{{
            background-image:url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-repeat:no-repeat;
            height: 100vh;
            }}
        </style>
        """

st.markdown(css, unsafe_allow_html=True)

st.session_state.setdefault('conversation_history', [])


def _extract_content(response):
    # Support dict-like or object-like responses from ollama
    try:
        if response is None:
            return None
        if isinstance(response, dict):
            # common shape: {'message': {'content': '...'}}
            msg = response.get('message')
            if isinstance(msg, dict):
                return msg.get('content')
            return response.get('content') or str(response)
        # fallback for objects with attributes
        if hasattr(response, 'message'):
            m = getattr(response, 'message')
            if isinstance(m, dict):
                return m.get('content')
            if hasattr(m, 'content'):
                return m.content
        if hasattr(response, 'content'):
            return response.content
        return str(response)
    except Exception:
        return None


def generate_response(user_input):
    st.session_state['conversation_history'].append({"role": "user", "content": user_input})

    try:
        response = ollama.chat(model="llama3.1:8b", messages=st.session_state['conversation_history'])
        ai_response = _extract_content(response)
        if not ai_response:
            ai_response = "(No response received from the model.)"
    except Exception as e:
        ai_response = f"Error contacting model: {e}"
        st.error(ai_response)
        st.text(traceback.format_exc())

    st.session_state['conversation_history'].append({"role": "assistant", "content": ai_response})
    return ai_response


def generate_affirmation():
    prompt = "Provide a positive affirmation to encourage someone who is feeling stressed or overwhelmed"
    try:
        response = ollama.chat(model="llama3.1:8b", messages=[{"role": "user", "content": prompt}])
        content = _extract_content(response)
        return content or "(No affirmation returned.)"
    except Exception as e:
        st.error(f"Affirmation error: {e}")
        return f"Affirmation error: {e}"


def generate_meditation_guide():
    prompt = "Provide a 5-minute guided meditation script to help someone relax and reduce stress."
    try:
        response = ollama.chat(model="llama3.1:8b", messages=[{"role": "user", "content": prompt}])
        content = _extract_content(response)
        return content or "(No meditation guide returned.)"
    except Exception as e:
        st.error(f"Meditation guide error: {e}")
        return f"Meditation guide error: {e}"


st.title("Mental Health Support Agent")

for msg in st.session_state['conversation_history']:
    role = "You" if msg['role'] == "user" else "AI"
    st.markdown(f"**{role}:** {msg['content']}")

user_message = st.text_input("How can I help you today?", key="user_message")

if user_message:
    with st.spinner("Thinking....."):
        ai_response = generate_response(user_message)
        st.markdown(f"**AI:** {ai_response}")

col1, col2 = st.columns(2)

with col1:
    if st.button("Give me a positive Affirmation"):
        affirmation = generate_affirmation()
        st.markdown(f"**Affirmation:** {affirmation}")

with col2:
    if st.button("Give me a guided meditation"):
        meditation_guide = generate_meditation_guide()
        st.markdown(f"**Guided Meditation:** {meditation_guide}")
