import streamlit as st
import requests

st.set_page_config(page_title="Customer Support Chatbot")

st.title("🤖 Customer Support Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("How can I help you today?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    try:
        res = requests.post(
            "http://127.0.0.1:8000/chat",   # ✅ MUST BE THIS
            json={"message": user_input},
            timeout=10
        )

        if res.status_code == 200:
            reply = res.json()["reply"]
        else:
            reply = f"❌ Backend error: {res.status_code}"

    except Exception as e:
        reply = "❌ Backend not reachable. Please ensure main.py is running on port 8000."

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
