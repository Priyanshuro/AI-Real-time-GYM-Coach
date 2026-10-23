
import streamlit as st
import sqlite3
from services.persistence.exercise_reprositry import get_or_create_user
def rander_login():
    if st.session_state.get("user_id"):
        return True

    st.title("🏋️ AI Real-time GYM Coach")
    st.write("Welcome! Please Enter Your Name")

    with st.form("login_form"):
        name = st.text_input("Name", placeholder="Enter your name")
        submit_button = st.form_submit_button("Start Session",width="stretch")

    if submit_button:
        if not name.strip():
            st.error("Please enter your name!")
            return False
        user=get_or_create_user(name.strip())
        st.session_state["name"] = user["name"]
        st.session_state["user_id"] =user["id"]
        st.rerun()

    return False
