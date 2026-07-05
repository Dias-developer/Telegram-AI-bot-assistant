from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram import Router, F
from aiogram.types import Message
from code_structure.state.states import user_mode
menu_router = Router()
def menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💬 AI Ассистент")],
            [KeyboardButton(text="✍️ Генератор текста")],
        ],
        resize_keyboard=True,
    )
    return keyboard

@menu_router.message(F.text == '💬 AI Ассистент')
async def ai_assistant(message: Message):
    user_mode[message.from_user.id] = "chat"
    await message.answer("Режим: 💬 AI Ассистент")

@menu_router.message(F.text == '✍️ Генератор текста')
async def texter(message: Message):
    user_mode[message.from_user.id] = "text"
    await message.answer("Режим: ✍️ Генератор текста")