import asyncio
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from dotenv import load_dotenv

from logging_bot import logger
from keyboard_bot import start_work, main_menu, quantity_selection
from sql import current_pay, new_period, close_period
from scripts import date

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
        self.dp.message.register(self.current_pay_main, F.text == "Текущий заработок")
        # self.dp.message.register(self.new_entry_main, F.text == "Начать запись дня")
        self.dp.message.register(self.other_text)

    ##Start
    async def start(self, message: types.Message):
        logger.info(f"Message /start {message.from_user.username}")
        await message.answer(
            f"Здравствуй, {message.from_user.username}.", reply_markup=self.start_work
        )

    ##переход в главное меню
    async def return_main_menu(self, message: types.Message):
        logger.info(f"return menu {message.from_user.username}")
        await message.answer(
            f"Вы в главном меню, {message.from_user.username}",
            reply_markup=self.main_menu,
        )

    ##запуск нового периода.
    ##Создание новой таблицы с именем id пользователя
    async def new_period_main(self, message: types.Message):
        id = int(message.from_user.id)
        try:
            new_period(id)
            logger.info(f"Создание нового периода пользователем {id}")
            await message.answer(
                f"{message.from_user.username}, запущен новый период {date()}."
            )
        except Exception as e:
            logger.error(
                f"При создании периода в main пользователем {id} произошла ошибка; {e}"
            )

    ##Выведение итогов периода и удаление таблицы
    async def close_period_main(self, message: types.Message):
        id = int(message.from_user.id)
        try:
            total = close_period(id)
            await message.answer(
                f"{message.from_user.username}, на {date()} твой заработок составил {total}.\nПериод закрыт."
            )
            logger.info(f"Пользователь {id} закрыл период")
        except Exception as e:
            logger.error(
                f"При попытке закончить период пользователем {id} произошла ошибка: {e}"
            )

    async def current_pay_main(self, message: types.Message):
        try:
            id = message.from_user.id
            current = current_pay(int(id))
            await message.answer(f"Заработок на {date()} составляет {current}")
            logger.info(f"Пользователь {id} вывел промежуточный заработок")
        except Exception as e:
            logger.error(
                f"Ошибка в main при попытке пользователя {id} вывести промежуточный заработок: {e}"
            )

    ##прием разного текста
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
