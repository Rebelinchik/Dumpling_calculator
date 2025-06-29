import sqlite3
import os


from dotenv import load_dotenv
from logging_bot import logger

load_dotenv()
db_path = os.getenv("SQL_FOLDER")
connect_db = sqlite3.connect(db_path)


##создание таблицы
def create_table(id: int):
    try:
        with connect_db as conn:
            cur = conn.cursor()
            cuery = f"CREATE TABLE a{str(id)} (id INTEGER PRYMARY KEY, total INTEGER)"
            cur.execute(cuery)
            conn.commit()
        logger.info(f"Создана таблица пользователем {id}")
    except Exception as e:
        logger.error(f"Ошибка создания новой таблицы пользователем {id}: {e}")


##Удаление таблицы
def delete_table(id: int):
    try:
        with connect_db as conn:
            cur = conn.cursor()
            cuery = f"DROP TABLE a{str(id)}"
            cur.execute(cuery)
            conn.commit()
        logger.info(f"Удалена таблица пользователем {id}")
    except Exception as e:
        logger.error(f"Ошибка при удалении таблицы пользователем {id}: {e}")


##заполнение первой строки пустым значением
def new_period(id: int):
    create_table(id)
    try:
        with connect_db as conn:
            cur = conn.cursor()
            cuery = f"INSERT INTO a{str(id)} (id, total) VALUES (?, ?)"
            params = (id, 0)
            cur.execute(cuery, params)
        logger.info(f"Пользователь {id} добавил первые значения в таблицу")
    except Exception as e:
        logger.error(f"При заполнении таблицы {id} произошла ошибка: {e}")


##внесение дневного заработка
def new_entry(id: int, score: int):
    pass


##считывание итогового заработка и удаление таблицы
def close_period(id: int):
    try:
        with connect_db as conn:
            cur = conn.cursor()
            cuery = f"SELECT total FROM a{str(id)}"
            cur.execute(cuery)
            total = cur.fetchone()[0]
        delete_table(id)
        logger.info(f"Пользоваель {id} законил период")
        return str(total)
    except Exception as e:
        logger.error(
            f"При попытке пользователя {id} закончить период произошла ошибка; {e}"
        )


##считываение данных
def current_pay(id: int):
    try:
        with connect_db as conn:
            cur = conn.cursor()
            cuery = f"SELECT total FROM a{str(id)}"
            cur.execute(cuery)
            total = cur.fetchone()[0]
        logger.info(f"Пользователь {id} вывел текущий заработок")
        return str(total)
    except Exception as e:
        logger.error(
            f"Ошибка при попытке пользователя {id} вывести текущий заработок: {e}"
        )
