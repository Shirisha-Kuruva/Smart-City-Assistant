import streamlit as st

def show_summary_card():
    st.header("🔍 Smart Search or Summary Card")
    st.markdown("### 🌇 Smart City Summary")

    # Display key metrics in 3 columns
    col1, col2, col3 = st.columns(3)

    col1.metric("⚡ Energy Saved", "1,200 kWh", "↑ 10%")
    col2.metric("💧 Water Saved", "8,000 L", "↑ 5%")
    col3.metric("♻️ Waste Recycled", "2 Tons", "↑ 12%")

    # Placeholder for future smart search or document embedding features
    st.write("🔎 This section will later support smart search or document summaries using vector embeddings or GPT-powered Q&A.")
