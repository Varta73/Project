import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    ("number", "expected"),
    [
      ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
      ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
      ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
      ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
      ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353")
    ])


def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected
    assert get_mask_card_number("7158300734726758") == "Некорректные данные"
    assert get_mask_card_number("Visa Gold 599941422842635") == "Некорректные данные"
    assert get_mask_card_number(" ") == "Некорректные данные"


@pytest.mark.parametrize(
    ("number_1", "expected_1"),
    [
      ("Счет 64686473678894779589", "Счет **9589"),
      ("Счет 35383033474447895560", "Счет **5560"),
      ("Счет 73654108430135874305", "Счет **4305")
    ])


def test_get_mask_account(number_1, expected_1):
    assert get_mask_account(number_1) == expected_1
    assert get_mask_account(" ") == "Некорректные данные"
    assert get_mask_account("7158300734726758") == "Некорректные данные"
    assert get_mask_account("Счет 6468647367889477958") == "Некорректные данные"

