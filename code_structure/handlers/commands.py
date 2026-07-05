from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from code_structure.keyboard.menu import menu

router = Router()

@router.message(CommandStart())
async def greeting(message: Message):
    await message.answer("Привет! Я твой AI-бот 🤖\n"
                        "Ниже в меню есть режимы!", reply_markup=menu())