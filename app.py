
import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Page settings
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI Chat Assistant")
st.write("Ask anything and get an AI-powered response.")

# Get Groq API key from .env
api_key = os.getenv("GROQ_API_KEY")

# Check API key
if not api_key:
    st.error("GROQ_API_KEY not found in .env file.")
    st.stop()

# Create Groq client
client = Groq(api_key=api_key)

# User input
user_message = st.text_area(
    "Enter your question:",
    placeholder="Type your question here..."
)

# Send button
if st.button("🚀 Send"):

    if not user_message.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner("🤔 AI is thinking..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            )

            answer = response.choices[0].message.content

        st.success("🤖 AI Response")
        st.write(answer)

