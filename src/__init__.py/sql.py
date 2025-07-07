import sqlite3
import os


from dotenv import load_dotenv
from logging_bot import logger

load_dotenv()
db_path = os.getenv("SQL_FOLDER")
connect_db = sqlite3.connect(db_path)


##Проверка на наличие таблицы пользователя
def ischek_table(id: int) -> bool:
    try:
        table_name = f"a{str(id)}"
        with connect_db as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                (table_name,),
            )
            result = cur.fetchone() is not None
            logger.info(f"При проверка наличия таблицы {result}")
            return result
    except Exception as e:
        logger.error(
            f"При проверке наличия таблицы {f"a{str(id)}"} произошла ошибка: {e}"
        )


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
def new_entry(id: int, text: int):
    try:
        with connect_db as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT total FROM a{id}")
            row = cur.fetchone()

            if row is None:
                raise ValueError(f"Пользователь с ID {id} не найден")

            total = row[0]

            if text == 2200:
                new_total = total + text
            else:
                new_total = total + ((text * 70) + 200)

            cur.execute(f"UPDATE a{id} SET total = ? WHERE id = ?", (new_total, id))
            conn.commit()  # Добавление commit для сохранения изменений

            logger.info(f"Пользователь {id} успешно добавил дневной заработок")

    except Exception as e:
        logger.error(
            f"При попытке пользователя {id} добавить дневной заработок произошла ошибка: {e}"
        )


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
