from openai import OpenAI
from dotenv import load_dotenv
import os

# 1. Load the .env file into environment variables
load_dotenv()

# 2. Get the API key from environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment. Check your .env file.")

# 3. Pass the key explicitly to the client
client = OpenAI(api_key=api_key)

# 4. Test request
resp = client.responses.create(
    model="gpt-4o-mini",
    input="Say hello in one line"
)

print(resp.output_text)
