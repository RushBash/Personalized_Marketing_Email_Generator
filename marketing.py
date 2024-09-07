import streamlit as st
import google.generativeai as genai
import os

# Load your Gemini API key from environment variable or other secure location
gemini_api_key ="AIzaSyApBJy59O2RT1mkRg5mj2dSdjLSU8U4ceU"
genai.configure(api_key=gemini_api_key)

st.title("Personalized Marketing Email Generator")

# Input fields
customer_name = st.text_input("Customer Name")
product_name = st.text_input("Product Name")
features = st.text_area("Product Features (comma-separated)")
tone = st.selectbox("Select Tone", ["Friendly", "Professional", "Excited"])

if st.button("Generate Email"):
    if not customer_name or not product_name or not features:
        st.error("Please fill in all the fields.")
    else:
        # Create the prompt for Gemini
        prompt = (
            f"Write a {tone.lower()} marketing email to {customer_name} promoting the product {product_name}. "
            f"Highlight the following features: {features}."
            f"You are writting this email representing a company called Flipzone. do not print [Your Name] after thanking the customer."
            f"Add subject line without fail at the begining of the email."
        )

        # Use the Gemini SDK to generate the response of a Email.
        model = genai.GenerativeModel(model_name='gemini-pro')
        genai.configure(api_key=gemini_api_key)
        response = model.generate_content(prompt)

        # Display the generated email
        if response:
            st.subheader("Generated Email:")
            st.write(response.text)
        else:
            st.error(f"Error: {response.get('error')}")