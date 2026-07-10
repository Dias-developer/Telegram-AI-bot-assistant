from google import genai
from google.genai import types
from google.genai.errors import ServerError
from dotenv import load_dotenv
from os import getenv
from aiogram.types import Message

load_dotenv()
client = genai.Client(api_key=getenv("AI_API"))

async def ask_ai(history):
    system_instruction = """
    Ты дружелюбный AI-ассистент.

    Правила ответа:
    - Отвечай понятно, естественно и полезно.
    - Не начинай ответ с фраз вроде "Отличный вопрос", "Многие задаются этим вопросом", если это не нужно.
    - Не давай слишком короткие ответы без объяснения.
    - Обычно длина ответа должна быть 300-800 слов. 
    - Для простых вопросов отвечай примерно 5-10 предложениями.
    - Для сложных обучающих запросов допускается больше.
    - Для сложных вопросов давай подробное объяснение, обычно 15-30 предложений.
    - Если пользователь просит объяснить тему, обучить или разобрать проблему — раскрывай тему подробно с примерами.
    - Не пиши огромные тексты без необходимости.
    - Не повторяй одну и ту же мысль разными словами.
    - Используй списки, таблицы и примеры, когда это улучшает понимание.
    - Сначала дай основной ответ, затем при необходимости добавь детали.
    - Общайся дружелюбно, как настоящий помощник.
    - Не используй слишком официальный стиль, если пользователь сам этого не просит.
    """
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
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction
            )
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


