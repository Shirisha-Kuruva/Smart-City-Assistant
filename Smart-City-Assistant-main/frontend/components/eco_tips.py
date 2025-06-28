import streamlit as st
import requests

def show_eco_tips():
    st.title("🌿 Eco-Friendly Tips Assistant")

    query = st.text_input("Enter a topic (e.g., recycling, water, plastic):")
    if st.button("Get Eco Tip"):
        response = requests.get("http://127.0.0.1:8000/eco/", params={"query": query})

        if response.status_code == 200:
            data = response.json()
            tips = data.get("tips", [])
            if tips:
                for tip in tips:
                    st.success(f"🌱 {tip}")
            else:
                st.warning("No tips found.")
        else:
            st.error("Failed to fetch tips.")
