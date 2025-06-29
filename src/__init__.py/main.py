import asyncio
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from dotenv import load_dotenv

from logging_bot import logger
from keyboard_bot import start_work, main_menu, quantity_selection

load_dotenv()
TOKEN = os.getenv("TOKEN")


class TelegramBot:
    def __init__(self):
        self.bot = Bot(TOKEN)
        self.dp = Dispatcher()

        # keyboard
        self.start_work = start_work
        self.main_menu = main_menu
        self.quantity_selection = quantity_selection

        self.register_handler()

    def register_handler(self):
        self.dp.message.register(self.start, Command("start"))
        self.dp.message.register(self.return_main_menu, F.text == "В главное меню")
        self.dp.message.register(self.new_period_main, F.text == "Начать период")
        self.dp.message.register(self.close_period_main, F.text == "Закончить период")
        self.dp.message.register(self.current_pay, F.text == "Текущий заработок")
        self.dp.message.register(self.new_entry_main, F.text == "Начать запись дня")
        self.dp.message.register(self.kg29, F.text == "29")
        self.dp.message.register(self.kg30, F.text == "30")
        self.dp.message.register(self.kg31, F.text == "31")
        self.dp.message.register(self.kg32, F.text == "32")
        self.dp.message.register(self.kg33, F.text == "33")
        self.dp.message.register(self.kg34, F.text == "34")
        self.dp.message.register(self.kg35, F.text == "35")
        self.dp.message.register(self.kg36, F.text == "36")
        self.dp.message.register(self.kg37, F.text == "37")
        self.dp.message.register(self.kg38, F.text == "38")
        self.dp.message.register(self.kg39, F.text == "39")
        self.dp.message.register(self.kg40, F.text == "40")

        self.dp.message.register(self.other_text)

    async def start(self, message: types.Message):
        logger.info(f"Message /start {message.from_user.username}")
        await message.answer(
            f"Здравствуй, {message.from_user.username}.", reply_markup=self.start_work
        )

    async def return_main_menu(self, message: types.Message):
        logger.info(f"return menu {message.from_user.username}")
        await message.answer(
            f"Вы в главном меню, {message.from_user.username}",
            reply_markup=self.main_menu,
        )

    async def new_period_main(self, message: types.Message):
        pass

    async def close_period_main(self, message: types.Message):
        pass

    async def other_text(self, message: types.Message):
        logger.info(f"message reply {message.from_user.username}")
        await message.answer(
            f"Управляй мной только с помощью клавиатуры. \nТвоё сообщение: {message.text}"
        )

    async def run(self):
        logger.info("Bot start")
        await self.dp.start_polling(self.bot)


if __name__ == "__main__":
    try:
        bot = TelegramBot()
        asyncio.run(bot.run())
    except Exception as e:
        logger.error(e)
