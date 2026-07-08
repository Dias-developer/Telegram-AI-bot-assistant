from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from code_structure.keyboard.menu import menu
from code_structure.state.memory import clear_history
router = Router()

@router.message(CommandStart())
async def greeting(message: Message):
    await message.answer("Привет! Я твой AI-бот 🤖\n"
                        "Ниже в меню есть режимы!", reply_markup=menu())


@router.message(Command('about'))
async def about(message: Message):
    await message.answer(
        "🤖 <b>AI Friend Bot</b>\n\n"
        "Я — AI-ассистент на базе Google Gemini.\n\n"
        "✨ Возможности:\n"
        "• 💬 Отвечаю на вопросы\n"
        "• ✍️ Генерирую тексты\n"
        "• 🧠 Помню контекст разговора\n"
        "• 🗑 Команда /clear очищает память\n\n"
        "📚 Этот бот создан в рамках курса\n"
        "«С нуля до AI-бота в Telegram».\n\n"
        "👨‍💻 Автор: Dias",
        parse_mode="HTML"
    )


@router.message(Command('clear'))
async def clear(message: Message):
    clear_history(message.from_user.id)

    await message.answer(
        "🗑 История диалога очищена!\n"
        "Теперь AI начнет разговор заново.\n"
        "Можете начать разговаривать после нажатия на один из режимов!"
    )