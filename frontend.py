import streamlit as st
import requests

# Streamlit app title
st.title("Chat with AI Assistant")

# Input text box for user message
user_message = st.text_input("Enter your message:")

# Button to send the message
if st.button("Send"):
    if user_message:
        try:
            # Send the message to the FastAPI backend
            response = requests.post(
    "https://ai-chatbot-ldjt.onrender.com/chat",
    json={"message": user_message}
)
            # Display the response from the backend
            if response.status_code == 200:
                st.success(response.json().get("response", "No response received"))
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a message before sending.")