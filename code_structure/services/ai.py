from google import genai
from dotenv import load_dotenv
from os import getenv

load_dotenv()
client = genai.Client(api_key=getenv("AI_API"))

