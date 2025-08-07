from dotenv import load_dotenv
import openai
import os

load_dotenv()
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
