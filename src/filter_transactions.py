import json
import re
from collections import Counter
from typing import Dict, List


def get_filter_transaction_description(transactions: list[dict], operations: str) -> list[dict]:
    """Функция, принимающая список словарей с данными о банковских операциях и строку поиска,
    и возвращающая список словарей, у которых в описании есть данная строка"""
    banking_operations = []
    for transaction in transactions:
        if "description" in transaction and re.search(operations, transaction["description"], flags=re.IGNORECASE):
            banking_operations.append(transaction)
    return banking_operations


def get_transaction_counter(transactions: list[dict], category: list) -> dict:
    """Функция, принимающая список словарей с данными о банковских операциях и список категорий операций,
    а возвращающая словарь, в котором ключи — это названия категорий,
     а значения — это количество операций в каждой категории."""
    list_category = []
    counter_category = {}
    for transaction in transactions:
        if transaction.get("description") in category:
            list_category.append(transaction.get("description"))
            counter_category = Counter(list_category)
    return counter_category


if __name__ == "__main__":
    with open("..\\data\\operations.json", encoding="UTF-8") as f:
        transactions = json.load(f)
        banking_operations = get_filter_transaction_description(transactions, "Перевод организации")
        print(banking_operations)


if __name__ == "__main__":
    with open("..\\data\\operations.json", encoding="UTF-8") as f:
        transactions = json.load(f)
        category = [
            "Перевод организации", "Перевод с карты на карту",
            "Открытие вклада","Перевод с карты на счет","Перевод со счета на счет"]
        counter_category = get_transaction_counter(transactions,category)
        print(counter_category)
