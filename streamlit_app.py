import streamlit as st
import google.generativeai as genai

# Configure the API key securely from Streamlit's secrets
# Make sure to add GOOGLE_API_KEY in secrets.toml (for local) or Streamlit Cloud Secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Streamlit App UI
st.title("Ever AI")
st.write("Use enerative AI to get responses based on your prompt.")

# Prompt input field
prompt = st.text_input("Enter your prompt:", "Best alternatives to javascript?")

# Button to generate response
if st.button("Generate Response"):
    try:
        # Load and configure the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Generate response from the model
        response = model.generate_content(prompt)
        
        # Display response in Streamlit
        st.write("Response:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
