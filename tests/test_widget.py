import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(number: str, expected: str) -> None:
    assert mask_account_card(number) == expected
    assert mask_account_card("7158300734726758") == "Некорректные данные"
    assert mask_account_card("Visa Gold 599941422842635") == "Некорректные данные"
    assert mask_account_card(" ") == "Некорректные данные"
    assert mask_account_card("7158300734726758") == "Некорректные данные"


@pytest.mark.parametrize(
    ("data", "expected1"),
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-05-29T02:20:00.690518", "29.05.2024"),
        ("2024-07-30T02:19:20.753951", "30.07.2024"),
    ],
)
def test_get_data(data: str, expected1: str) -> None:
    assert get_data(data) == expected1
    assert get_data(" ") == "Некорректный формат даты"
    assert get_data("2024-03-T02:26:18.671407") == "Некорректный формат даты"
