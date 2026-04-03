import streamlit as st
import requests
import uuid

st.title("Chat with AI Assistant")

if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

user_message = st.text_input("Enter your message:")

if st.button("Send"):
    if user_message:
        try:
            response = requests.post(
                "https://ai-chatbot-ldjt.onrender.com/chat",
                json={
                    "message": user_message,
                    "user_id": st.session_state.user_id
                },
                timeout=30,
                headers={"Connection": "close"}   # 🔥 ADD THIS LINE
            )

            if response.status_code == 200:
                st.success(response.json().get("response", "No response received"))
            else:
                st.error(f"Error: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"Connection error: {e}")

    else:
        st.warning("Please enter a message before sending.")