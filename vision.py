import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
from google import genai

load_dotenv()

st.set_page_config(page_title="Gemini Vision", page_icon="🖼️", layout="centered")
st.title("🖼️ Gemini Image Understanding")
st.write("Upload an image and ask Gemini to describe or analyze it.")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY is missing. Add it to your local .env file.")
    st.stop()

client = genai.Client(api_key=api_key)
model_name = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg", "webp"])
prompt = st.text_area("What would you like to know about this image?",
                      value="Describe this image clearly and list the important details.")

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)

    if st.button("Analyze image", type="primary"):
        try:
            with st.spinner("Analyzing image..."):
                response = client.models.generate_content(
                    model=model_name,
                    contents=[prompt, image],
                )
            st.subheader("Gemini's response")
            st.markdown(response.text or "No text response returned.")
        except Exception as exc:
            st.error(f"Image analysis failed: {exc}")
