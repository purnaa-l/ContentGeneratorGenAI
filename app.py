from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load Gemini Pro Model and get Responses
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question )
    return response.text 

#initalise our streamlit app

st.set_page_config(page_title="Q&A demo")
st.header("Gemini LLM Model")
input=st.text_input("Input: ", key="input")
submit=st.button("Ask Questions!")

#when submit clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("the response is")
    st.write(response)
