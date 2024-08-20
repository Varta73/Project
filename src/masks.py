from typing import Optional
import logging
import os

dir1 = os.path.dirname(os.path.abspath(__file__))
path_1 = os.path.join(dir1, "../src/masks.log")
path_2 = os.path.abspath(path_1)

# Логгер, который записывает логи в файл.
logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(path_2, "w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> Optional[str]:
    """Функция маскировки номера банковской карты"""
    if len(card_number) == 24 or len(card_number) > 25:
        return (
            f"{card_number[:-17]} {card_number[-16:-12]} {card_number[-12:-10]}{'*' * 2} {'*' * 4} {card_number[-4:]}"
        )
    else:
        return "Некорректные данные"


def get_mask_account(acc_number: str) -> Optional[str]:
    """Функция маскировки номера банковского счёта"""
    if "Счет" in acc_number or len(acc_number) == 25:
        return f"Счет {'*' * 2}{acc_number[-4::]}"
    else:
        return "Некорректные данные"

