import streamlit as st

def apply_background():

    st.markdown(
        """
        <style>

        /* Calm Dark Blue Gradient */

        .stApp {
            background: linear-gradient(
                180deg,
                #0F2027,
                #203A43,
                #2C5364
            );
            background-size: 200% 200%;
            animation: darkBlueGradient 10s ease-in-out infinite alternate;
        }

        @keyframes darkBlueGradient {
            0% {background-position: top;}
            100% {background-position: bottom;}
        }

        </style>
        """,
        unsafe_allow_html=True
    )