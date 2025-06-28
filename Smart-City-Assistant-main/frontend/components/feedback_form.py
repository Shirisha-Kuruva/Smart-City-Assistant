import streamlit as st
import requests

def show_feedback_form():
    st.title("📝 Citizen Feedback")

    name = st.text_input("Your Name")
    issue = st.selectbox("Type of Issue", ["Garbage", "Water", "Electricity"])
    desc = st.text_area("Describe the issue")

    if st.button("Submit Feedback"):
        payload = {"username": name, "feedback": desc}
        response = requests.post("http://127.0.0.1:8000/feedback/", json=payload)
        if response.status_code == 200:
            st.success("Thanks for your feedback!")
        else:
            st.error("Submission failed.")
