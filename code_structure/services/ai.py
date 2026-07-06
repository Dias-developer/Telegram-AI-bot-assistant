from google import genai
from dotenv import load_dotenv
from os import getenv
from aiogram.types import Message

load_dotenv()
client = genai.Client(api_key=getenv("AI_API"))

async def ask_ai(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

async def send_long_messages(message: Message, text: str):
    max_length = 4096

    for i in range(0, len(text), max_length):
        await message.answer(text[i:i + max_length])


