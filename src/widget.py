from datetime import datetime

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
    dat = datetime.strptime(data, format("%Y-%m-%dT%H:%M:%S.%f"))
    return dat.strftime("%d.%m.%Y")


# print(get_data("2024-07-22T02:26:18.671407"))
