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
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(path_2, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def reader_csv_file(csv_file: str) -> list[Any]:
    """Функция принимает на вход путь к файлу CSV в качестве аргумента и возвращает список словарей с транзакциями"""
    with open(csv_path1, newline="", encoding="utf-8") as f:
        csv_result = []
        csv_dicts = {}
        try:
            reader_csv = csv.DictReader(f, delimiter=";")
            logger.info("Формат файла csv верный")
            for row in reader_csv:
                csv_dicts["id"] = row["id"]
                csv_dicts["state"] = row["state"]
                csv_dicts["date"] = row["date"]
                csv_dicts["amount"] = row["amount"]
                csv_dicts["currency_name"] = row["currency_name"]
                csv_dicts["currency_code"] = row["currency_code"]
                csv_dicts["from"] = row["from"]
                csv_dicts["to"] = row["to"]
                csv_dicts["description"] = row["description"]
                csv_result.append(csv_dicts)
            return csv_result
        except Exception:
            logger.warning("Некорректные данные")
    return []
print(reader_csv_file(csv_path1))