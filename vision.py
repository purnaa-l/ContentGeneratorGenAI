from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import pandas as pd

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model (update to the correct model if needed)
model = genai.GenerativeModel("gemini-1.5-flash")  # Updated model name

# Function to get responses from the model
def get_gemini_response(input_text, image):
    if input_text:
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text 

# Streamlit app setup
st.set_page_config(page_title="Image Generator Demo")
st.header("Gemini LLM Model")

# Input for text
input_text = st.text_input("Input: ", key="input")

# File uploader for images
uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "jpg", "png"])
image = None  # Initialize image variable

if uploaded_file is not None:
    # Read the file based on its type
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
        st.write("DataFrame:")
        st.dataframe(df)

    elif uploaded_file.name.endswith(('jpg', 'jpeg', 'png')):
        image = Image.open(uploaded_file)  # Store the uploaded image
        st.image(image, caption='Uploaded Image.', use_column_width=True)

    else:
        st.write("Uploaded file type not supported.")

# Button to submit input and get response
submit = st.button("Tell me about the image!")

if submit:
    if image is not None:  # Ensure an image is uploaded
        response = get_gemini_response(input_text, image)
        st.header("The response is:")
        st.write(response)
    else:
        st.warning("Please upload an image to get a response.")
