import streamlit as st
import requests

def show_anomaly_checker():
    st.header("🔍 Anomaly Detection")

    # Input fields
    metric = st.text_input("KPI Metric (e.g., Water Consumption)", "")
    value = st.number_input("Value", min_value=0.0, format="%.2f")

    if st.button("Check Anomaly"):
        if metric.strip() == "":
            st.warning("Please enter a valid KPI metric.")
            return

        payload = {
            "metric": metric,
            "value": value
        }

        try:
            response = requests.post("http://127.0.0.1:8000/anomaly/", json=payload)
            result = response.json()

            # Show raw backend response
            st.write("🔁 Backend Response:", result)

            # Handle the response properly
            if "anomaly" in result and "metric" in result:
                if result["anomaly"]:
                    st.error(f"⚠️ Anomaly Detected in {result['metric']}!")
                else:
                    st.success(f"✅ {result['metric']} is within normal range.")
            else:
                st.info("Anomaly check complete, but response format was unexpected.")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Could not connect to the backend: {e}")
