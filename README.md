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

## 🚀 Usage
python your_script_name.py

## 📤 Expected Output
Hello! 👋
(Output may vary depending on the model’s response.)

## 📂 Project Structure
openai-quickstart-agent/
│── your_script_name.py  # Main script
│── .env                 # Stores your OpenAI API key (DO NOT COMMIT)
│── README.md            # Documentation

## ⚠️ Important Notes
- Never share your `.env` file or API key publicly.  
- You can change the model from `gpt-4o-mini` to `gpt-5`, `gpt-4.1`, etc.  
- Requires an OpenAI API account with billing enabled.  

## 📜 License
Licensed under the MIT License — free to use and modify.

✨ Run it. Talk to AI. Build cool stuff. ✨
