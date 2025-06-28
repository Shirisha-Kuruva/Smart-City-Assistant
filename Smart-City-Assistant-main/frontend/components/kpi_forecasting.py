import streamlit as st
import pandas as pd
import requests

def show_kpi_uploader():
    st.header("📊 Upload KPI CSV")

    uploaded_file = st.file_uploader("Upload KPI CSV", type=["csv"])

    if uploaded_file is not None:
        try:
            # Read and preview the CSV
            df = pd.read_csv(uploaded_file)
            st.subheader("📄 CSV Preview")
            st.dataframe(df)

            # Upload the file to backend on button click
            if st.button("Submit"):
                response = requests.post(
                    "http://127.0.0.1:8000/kpi/",
                    files={"file": uploaded_file.getvalue()}
                )

                if response.status_code == 200:
                    st.success("✅ KPI data uploaded successfully!")
                else:
                    st.error(f"❌ Upload failed. Server responded with status: {response.status_code}")
        except Exception as e:
            st.error(f"⚠️ Error processing file: {e}")
