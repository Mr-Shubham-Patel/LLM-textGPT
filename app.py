from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()   ### load all environment variables from .env file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

### Initialize the app
st.set_page_config(page_title="LLM Project")

st.header("LLM Gemini Application Project")

input = st.text_input("Ask Something..",key="input")

submit = st.button("Submit")

### function to load the llm model, pass the question and get the response
def get_gemini_model_response(question):
    model = genai.GenerativeModel("gemini-2.0-flash-lite")
    response = model.generate_content(question)
    return response.text

if submit:
    model_response = get_gemini_model_response(input)
    st.write(model_response)