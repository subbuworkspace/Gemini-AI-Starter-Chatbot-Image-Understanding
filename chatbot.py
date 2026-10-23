import os
import time
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(page_title="Gemini AI Chatbot", page_icon="💬", layout="centered")
st.title("💬 Gemini AI Chatbot")
st.caption("A simple conversational app powered by Google's Gemini API.")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY is missing. Add it to your local .env file.")
    st.stop()

client = genai.Client(api_key=api_key)
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.button("Clear chat"):
    st.session_state.messages = []
    st.rerun()

question = st.chat_input("Ask Gemini a question...")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        try:
            with st.spinner("Waiting for Gemini..."):
                started = time.time()
                # Send recent conversation history so replies have context.
                history = []
                for item in st.session_state.messages[-11:]:
                    role = "user" if item["role"] == "user" else "model"
                    history.append({"role": role, "parts": [{"text": item["content"]}]})

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=history,
                )
                answer = getattr(response, "text", None) or "Gemini returned an empty response."
                elapsed = time.time() - started

            placeholder.markdown(answer)
            st.caption(f"Response time: {elapsed:.1f} seconds")
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as exc:
            placeholder.error(
                f"Gemini request failed: {exc}\n\n"
                "Check your API key, model availability, internet connection, and API quota."
            )
