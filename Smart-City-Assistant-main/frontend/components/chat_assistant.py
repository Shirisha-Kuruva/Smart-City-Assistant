import streamlit as st
import requests

def show_chat_assistant():
    st.header("🤖 Policy Chat Assistant")

    # Input field for user question
    user_input = st.text_input("Ask a question about sustainability:")

    # Button to send the question
    if st.button("Ask"):
        if user_input.strip() == "":
            st.warning("Please enter a question.")
            return

        try:
            # Send request to FastAPI backend with the correct key: "message"
            response = requests.post(
                "http://127.0.0.1:8000/chat/",
                json={"message": user_input}
            )
            result = response.json()

            # Display backend response for debugging
            st.write("🔁 Chat Response:", result)

            # Show the assistant's reply if successful
            if "response" in result:
                st.success(result["response"])
            else:
                st.error("Chat failed. Unexpected response format.")

        except Exception as e:
            st.error(f"Chat failed: {e}")
