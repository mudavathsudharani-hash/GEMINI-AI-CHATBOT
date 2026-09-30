import streamlit as st
from dotenv import load_dotenv
import os
from google import genai
load_dotenv()
api_key =os.getenv(" GEMINI_API_KEY")
client=genai.Client(api_key=api_key)
st.set_page_config(page_title="Gemini AI CHATBOT", layout="centered")
st.title("Gemini AI CHATBOT")
st.write("This is a simple chatbot application using Gemini AI.")
prompt= st.text_area("Enter your prompt here:",placeholder="explain artificial intelligence...")
if st.button("generate response"):
    if prompt:
        with st.spinner("Generating response"):
            response = client.models.generate_content(
                model="gemini-3.7-flash",
                contents=prompt,
            )
        st.success("Response generated successfully!")
        st.write(response.text)
    else:
        st.warning("Please enter a Prompt.")