from aiogram import Router
from aiogram.types import Message
from code_structure.state.states import user_mode
from code_structure.services.ai import client, ask_ai, send_long_messages

chat_router = Router()

@chat_router.message()
async def ai_chat(message: Message):
    mode = user_mode.get(message.from_user.id)

    if message.from_user.id not in user_mode:
        await message.answer("Выбери режим 👇")
        return

    if mode == "chat":

        response = await ask_ai(message.text)
        await send_long_messages(message, response)
    elif mode == "text":
        prompt = ("Ты профессиональный помощник по написанию текстов.\n"
                  f"Запрос пользователя: {message.text}"
                  )
        response = await ask_ai(prompt)
        await send_long_messages(message, response)