import sqlite3
import os


from dotenv import load_dotenv
from logging_bot import logger


load_dotenv()
db_path = os.getenv("SQL_FOLDER")
connect_db = sqlite3.connect(db_path)


def create_table(id: int):
    try:
        with connect_db as conn:
            cur = conn.cursor()
            cur.execute(
                f"""CREATE TABLE {id} (
                id INTEGER PRYMARY KEY,
                total INTEGER,
                )
"""
            )
            conn.commit()
        logger.info(f"Создана таблица пользователем {id}")
    except Exception as e:
        logger.error(f"Ошибка создания новой таблицы пользователем {id}: {e}")


def delete_table(id: int):
    try:
        with connect_db as conn:
            cur = conn.cursor()
            cur.execute(f"""DROP TABEL {id}""")
            conn.commit()
        logger.info(f"Удалена таблица пользователем {id}")
    except Exception as e:
        logger.error(f"Ошибка при удалении таблицы пользователем {id}: {e}")


def new_period(id: int):
    create_table(id)
    try:
        with connect_db as conn:
            cur = conn.cursor()
            cur.execute(f"INSERT INTO {id} (id, total) VALUES (?, ?)", (id, 0))
        logger.info(f"Пользователь {id} добавил первые значения в таблицу")
    except Exception as e:
        logger.error(f"При заполнении таблицы {id} произошла ошибка: {e}")


def new_entry(id: int, score: int):
    pass


def close_period(id: int):
    pass
