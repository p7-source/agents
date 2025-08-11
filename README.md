# agents
# 🤖 OpenAI Quickstart Agent ✨

A minimal Python script to connect with the OpenAI API using a securely stored API key. Loads your API key from a `.env` file, initializes the client, and sends a test prompt to GPT.

## 📌 Features
- 🔒 Secure API key handling via `.env` file  
- 💬 Sends a test request to `gpt-4o-mini`  
- 🐍 Works with Python 3.9+  
- ⚡ Lightweight — only needs `openai` & `python-dotenv`  
- 🛠 Ready to run inside a Conda environment  
- 📂 Clear project structure for easy setup  

## 🛠️ Setup Instructions
```bash
# 1. Create and activate Conda environment
conda create -n openai-agent python=3.11 -y
conda activate openai-agent

# 2. Install dependencies
pip install openai python-dotenv

# 3. Create .env file for API key
echo "OPENAI_API_KEY=sk-your-api-key-here" > .env
