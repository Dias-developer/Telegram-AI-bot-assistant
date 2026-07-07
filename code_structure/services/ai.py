from google import genai
from google.genai.errors import ServerError
from dotenv import load_dotenv
from os import getenv
from aiogram.types import Message

load_dotenv()
client = genai.Client(api_key=getenv("AI_API"))

async def ask_ai(history):
    if isinstance(history, str):
        contents = [
            {
                "role": "user",
                "parts": [
                    {"text": history}
                ]
            }
        ]

    else:
        contents = []

        for message in history:
            contents.append({
                "role": message["role"],
                "parts": [
                    {"text": message["text"]}
                ]
            })

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents
        )

        return response.text

    except ServerError:
        return "⚠️ AI сейчас перегружен. Попробуйте ещё раз через несколько секунд."
async def send_long_messages(message: Message, text: str):
    max_length = 4096

    text = text.replace("**", "")
    text = text.replace("##", "")
    text = text.replace("```", "")
    text = text.replace("---", "")
    text = text.replace("#", "")

    for i in range(0, len(text), max_length):
        await message.answer(text[i:i + max_length])


