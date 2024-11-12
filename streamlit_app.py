import streamlit as st
import google.generativeai as genai

# Configure the API key securely from Streamlit's secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Rest of the app code
st.title("Generative AI with Streamlit")
prompt = st.text_input("Enter your prompt:", "most powerful free tts?")
if st.button("Generate Response"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    st.write("Response:")
    st.write(response.text)
