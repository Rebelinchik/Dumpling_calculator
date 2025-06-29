from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_work = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="В главное меню")]],
    resize_keyboard=True,
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Начать период"), KeyboardButton(text="Закончить период")],
        [
            KeyboardButton(text="Текущий заработок"),
            KeyboardButton(text="Начать запись дня"),
        ],
    ],
    resize_keyboard=True,
)

quantity_selection = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="29"),
            KeyboardButton(text="30"),
            KeyboardButton(text="31"),
        ],
        [
            KeyboardButton(text="32"),
            KeyboardButton(text="33"),
            KeyboardButton(text="34"),
        ],
        [
            KeyboardButton(text="35"),
            KeyboardButton(text="36"),
            KeyboardButton(text="37"),
        ],
        [
            KeyboardButton(text="38"),
            KeyboardButton(text="39"),
            KeyboardButton(text="40"),
        ],
        [KeyboardButton(text="В главное меню")],
    ],
    resize_keyboard=True,
)
