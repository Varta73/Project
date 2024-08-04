from typing import Optional


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

