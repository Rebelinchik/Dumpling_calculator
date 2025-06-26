import logging

###создание логера
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

###обработчик для консоли
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

###формат сообщений и присвавание формата файлу и консоли
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

###добавляем обработчики в логер
logger.addHandler(console_handler)
