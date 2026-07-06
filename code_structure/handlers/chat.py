from aiogram import Router
from aiogram.types import Message
from code_structure.state.states import user_mode

chat_router = Router()

@chat_router.message()
async def ai_chat(message: Message):
    mode = user_mode.get(message.from_user.id)

    if message.from_user.id not in user_mode:
        await message.answer("Выбери режим 👇")
        return

    if mode == "chat":
        await message.answer("🤖 скоро будет ответ от AI")
    elif mode == "text":
        await message.answer("✍️ идет генерация текста...")
