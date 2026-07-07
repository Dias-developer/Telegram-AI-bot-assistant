from aiogram import Router
from aiogram.types import Message
from code_structure.state.states import user_mode
from code_structure.services.ai import ask_ai, send_long_messages
from code_structure.state.memory import (
    get_history,
    add_user_message,
    add_ai_message
)
chat_router = Router()

@chat_router.message()
async def ai_chat(message: Message):
    mode = user_mode.get(message.from_user.id)

    if mode is None:
        await message.answer("Выбери режим 👇")
        return

    if mode == "chat":

        user_id = message.from_user.id

        add_user_message(user_id, message.text)

        history = get_history(user_id)

        response = await ask_ai(history)

        add_ai_message(user_id, response)

        await send_long_messages(message, response)
    elif mode == "text":
        prompt = ("Ты профессиональный помощник по написанию текстов.\n"
                  f"Запрос пользователя: {message.text}"
                  )
        response = await ask_ai(prompt)
        await send_long_messages(message, response)