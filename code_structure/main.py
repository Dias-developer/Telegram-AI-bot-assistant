from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from os import getenv
import logging
import asyncio

from handlers.commands import router
from keyboard.menu import menu_router
from handlers.chat import chat_router

load_dotenv()
token = getenv("TOKEN")
dp = Dispatcher()

async def main():

    dp.include_router(router)
    dp.include_router(menu_router)
    dp.include_router(chat_router)

    bot = Bot(token=token)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print('Start...')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Stop...')