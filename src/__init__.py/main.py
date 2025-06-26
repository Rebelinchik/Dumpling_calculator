import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

from logging_bot import logger

load_dotenv()
TOKEN = os.getenv("TOKEN")


class TelegramBot:
    def __init__(self):
        self.bot = Bot(TOKEN)
        self.dp = Dispatcher()
        self.register_handler()

    def register_handler(self):
        self.dp.message.register(self.start, Command("start"))
        self.dp.message.register(self.reply)

    async def start(self, message: types.Message):
        logger.info("Message /start")
        await message.answer(f"Здравствуй, {message.from_user.id}.")

    async def reply(self, message: types.Message):
        logger.info("message reply")
        await message.answer(f"{message.text}")

    async def run(self):
        logger.info("Bot start")
        await self.dp.start_polling(self.bot)


if __name__ == "__main__":
    try:
        bot = TelegramBot()
        asyncio.run(bot.run())
    except Exception as e:
        logger.error(e)
