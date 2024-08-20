import json
from typing import Any
import json
from typing import Any
import logging
import os

dir1 = os.path.dirname(os.path.abspath(__file__))
path_1 = os.path.join(dir1, "../src/utils.log")
path_2 = os.path.abspath(path_1)

# Логгер, который записывает логи в файл.
logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(path_2, "w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def get_transaction(file_json: str) -> Any:
    """
    Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.

    """

    with open(file_json, encoding="utf-8") as f:
        try:
            trans = json.load(f)
            return trans

        except:
            return []


print(
    json.dumps(
        get_transaction(r"C:\Users\Светлана\PycharmProjects\pythonProject\data\operations.json"),
        indent=4,
    )
)
