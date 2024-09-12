from datetime import datetime

import os

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(string: str) -> str | None:
    """Функция маскировки номера карты или счета"""
    if "Счет" in string:
        acc_number = get_mask_account(string[:])
        return acc_number
    else:
        card_number = get_mask_card_number(string[:])
        return card_number


# print(mask_account_card("Счет 73654108430135874305"))


def get_data(data: str) -> str:
    """Функция принимает на вход данные о дате и времени и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"""
    if len(data) == 26:
        dat = datetime.strptime(data, format("%Y-%m-%dT%H:%M:%S.%f"))
        return dat.strftime("%d.%m.%Y")
    if len(data) == 20:
        dat = datetime.strptime(data, format("%Y-%m-%dT%H:%M:%SZ"))
        return dat.strftime("%d.%m.%Y")
    else:
        return "Некорректный формат даты"


# print(get_data("2020-08-02T09:35:18Z"))
