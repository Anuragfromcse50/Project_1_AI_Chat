🤖 AI Chat Assistant

An AI-powered chat assistant built with Python, Streamlit, Groq API,
and an open-weight AI model.

Project Overview

Project: AI Chat Assistant

Type: Generative AI / Chatbot

Frontend: Streamlit

AI API: Groq

Model: openai/gpt-oss-20b

Language: Python

Version Control: Git + GitHub

Deployment: Streamlit Community Cloud

Developed as part of preparation for MLH × GDG Hack Day Prayagraj
2026, focused on open-source/open-weight AI models, tools, and agents.

Features

Web-based AI chat interface

User question input

AI-generated responses

Loading indicator

Empty-input validation

API-key validation

Local .env support

Streamlit Cloud Secrets support

GitHub-ready project structure

Cloud deployment support

Technologies

Technology                  Purpose

Python                      Application language
Streamlit                   Web interface
Groq                        AI inference API
openai/gpt-oss-20b        AI model
python-dotenv               Local environment variables
Git                         Version control
GitHub                      Repository hosting
Streamlit Community Cloud   Deployment

Project Structure

Project_1_AI_Chat/
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
└── .env                 # Local only - never upload

Files

app.py

Main Streamlit application. It loads configuration, creates the Groq
client, accepts user input, sends the question to the model, and
displays the response.

main.py

Original desktop GUI version created before the Streamlit web interface.

requirements.txt

streamlit
groq
python-dotenv

.gitignore

.env
.venv/
.venv313/
__pycache__/

API Key Setup

Local

Create .env in the project root:

GROQ_API_KEY="YOUR_GROQ_API_KEY"

Never commit this file.

Streamlit Cloud

Add the key under App Settings → Secrets:

GROQ_API_KEY = "YOUR_GROQ_API_KEY"

Use valid TOML and do not include the Markdown code fences.

Run Locally

Open PowerShell:

cd "C:\Users\Hp\OneDrive\Desktop\HackDay_2026\Project_1_AI_Chat"

Then:

streamlit run app.py

The application normally opens at:

http://localhost:8501

Do not use python app.py to start the Streamlit version.

How to Use

Open the application.

Enter a question.

Click 🚀 Send.

Wait for the AI response.

Read the generated answer.

Example:

What is Artificial Intelligence?

GitHub

The project uses the main branch.

Typical workflow:

git status
git add .
git commit -m "Update AI Chat Assistant"
git push

Deployment

For Streamlit Community Cloud:

Repository: Anuragfromcse50/Project_1_AI_Chat
Branch: main
Main file: app.py

After deployment, configure GROQ_API_KEY in Streamlit Secrets.

Security

Never upload API keys, .env, passwords, or private tokens.

The .gitignore file protects .env from being staged by Git.

If an API key is accidentally exposed, revoke it and create a new key.

Future Improvements

Chat history

Conversation memory

Streaming responses

Model selection

Custom system prompts

File/document Q&A

Voice input/output

AI agent tools

Authentication

Better error handling

Hackathon Value

This project demonstrates Generative AI integration, API-based
inference, Python development, Streamlit UI, secret management,
Git/GitHub workflow, and cloud deployment.

Author

Anurag

Built with Python and open-weight AI technologies for HackDay 2026
preparation.


link - https://anuragfromcse50-project-1-ai-chat-app-zav28g.streamlit.app/
