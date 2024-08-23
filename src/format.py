import csv
import logging
import os
from typing import Any

import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
path_1 = os.path.join(current_dir, "../logs/format.log")
path_2 = os.path.abspath(path_1)

# Создаем путь до файла csv относительно текущей директории
csv_path = os.path.join(current_dir, "../data/transactions.csv")
csv_path1 = os.path.abspath(csv_path)

# Создаем путь до файла xlsx относительно текущей директории
xlsx_path = os.path.join(current_dir, "../data/transactions_excel.xlsx")
xlsx_path1 = os.path.abspath(xlsx_path)

# Логер, который записывает логи в файл.
logger = logging.getLogger("format")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(path_2, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def reader_csv_excel(file_name: str) -> list[dict[Any, Any]]:
    """Принимает путь к файлу csv либо xlsx с информацией о транзакциях.
    Возвращает список словарей транзакций."""
    logger.info("Программа начинает работу.")
    # Определяем тип файла и применяем необходимый метод обработки.
    if file_name.endswith("csv"):
        csv_result = []
        with open(csv_path1, newline="", encoding="utf-8") as f:
            try:
                logger.info("Программа считывает csv файл.")
                reader_csv = csv.DictReader(f, delimiter=";")
                for row in reader_csv:
                    logger.info("Программа формирует список транзакций по считанным из файла данным.")
                    csv_result.append(row)
                    logger.info("Программа успешно завершила свою работу.")
                return csv_result
            except Exception as err:
                logger.error(f"При считывании файла произошла ошибка {err}.")
    elif file_name.endswith("xlsx"):
        try:
            logger.info("Программа считывает xlsx файл.")
            df_dict = pd.read_excel(xlsx_path1, index_col=0)
            logger.info("Программа формирует список транзакций по считанным из файла данным.")
            list_of_dicts = df_dict.to_dict("records")
            logger.info("Программа успешно завершила свою работу.")
            return list_of_dicts
        except Exception as err:
            logger.error(f"При считывании файла произошла ошибка {err}.")
    else:
        logger.error("Произошла ошибка ValueError: Неподдерживаемый формат файла.")
        raise ValueError("Неподдерживаемый формат файла.")


# print(reader_csv_excel(csv_path1))
