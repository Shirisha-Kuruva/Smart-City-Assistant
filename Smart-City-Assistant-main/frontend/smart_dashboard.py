import streamlit as st
from components.chat_assistant import show_chat_assistant
from components.kpi_forecasting import show_kpi_uploader
from components.anomaly import show_anomaly_checker
from components.feedback_form import show_feedback_form
from components.summary_card import show_summary_card  # optional

# Sidebar navigation
st.sidebar.title("🌆 Smart City Assistant")
page = st.sidebar.radio("Navigate", [
    "Policy Chat Assistant",
    "Upload KPI CSV",
    "Anomaly Detection",
    "Submit Feedback",
    "Smart Search"
])

# Routing to pages
if page == "Policy Chat Assistant":
    show_chat_assistant()

elif page == "Upload KPI CSV":
    show_kpi_uploader()

elif page == "Anomaly Detection":
    show_anomaly_checker()

elif page == "Submit Feedback":
    show_feedback_form()

elif page == "Smart Search":
    show_summary_card()
