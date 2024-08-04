from typing import Any, Generator

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency1(trans_list_1: list) -> None:
    generator = filter_by_currency(trans_list_1, "USD")
    assert next(generator) == (
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    )
    assert next(generator) == (
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    )
    assert next(generator) == (
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    )


def test_filter_by_currency2(trans_list_2: list) -> None:
    generator = filter_by_currency(trans_list_2, "USD")
    assert list(generator) == []


def test_filter_by_currency3(trans_list_1: list) -> None:
    generator = filter_by_currency(trans_list_1, "EUR")
    assert generator != "Нет транзакций"


def test_transaction_descriptions1(trans_list_1: list) -> None:
    gen = transaction_descriptions(trans_list_1, "description")
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод с карты на карту"
    assert next(gen) == "Перевод организации"


def test_transaction_descriptions2(trans_list_2: list) -> None:
    gen = transaction_descriptions(trans_list_2, "description")
    assert list(gen) == []


def test_card_number_generator() -> None:
    gener = card_number_generator(1, 2)
    assert next(gener) == "0000 0000 0000 0001"
    assert next(gener) == "0000 0000 0000 0002"


def test_card_number_generator1() -> None:
    gener = card_number_generator(-1, 1)
    assert next(gener) == "0000 0000 0000 0001"
