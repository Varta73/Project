from typing import Any, Generator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: list, code: str) -> Generator[Any, Any, Any]:
    """Функция выдает транзакции, где валюта операции соответствует заданной."""
    for i in transactions:
        if i.get("operationAmount").get("currency").get("code") == code:
            yield i


i_transactions = filter_by_currency(transactions, "EUR")
if transactions != []:
    while True:
        try:
            print(next(i_transactions))
        except StopIteration:
            print("Транзакций с заданными условиями нет")
            break
else:
    print("Нет транзакций")


def transaction_descriptions(transactions: list, description: str) -> Generator[Any, Any, Any]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


i_transactions = transaction_descriptions(transactions, "description")
if transactions != []:
    while True:
        try:
            print(next(i_transactions))
        except StopIteration:
            print(" ")
            break
else:
    print("Нет транзакций")


def card_number_generator(start: int, stop: int) -> Generator[Any, Any, Any]:
    """Функция генерации номеров карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for x in range(start, stop + 1):
        zero = "0000000000000000"
        str_sum = zero + str(x)
        if x <= 0:
            print("Номер карты не может быть отрицательным или нулевым")
        else:
            card_number = f"{str_sum[-16:-12]} {str_sum[-12:-8]} {str_sum[-8:-4]} {str_sum[-4:-1]}{str_sum[-1]}"
            yield card_number


for card_number in card_number_generator(-3, 3):
    print(card_number)
