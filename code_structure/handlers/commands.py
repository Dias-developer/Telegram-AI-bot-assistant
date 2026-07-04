from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

router = Router()

@router.message(CommandStart())
async def greeting(message: Message):
    await message.answer("Hello")