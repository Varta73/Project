from unittest.mock import patch, Mock

import pytest

from src.format import reader_csv_excel


@patch('pandas.read_csv')
def test_reader_csv_excel(mock_read_csv):
    """Тестируем считывание csv-файла"""
    mock_read_csv = Mock([
        {"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z", "amount": "16210"}
    ])

    assert reader_csv_excel(mock_read_csv) == [
            {"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z", "amount": "16210"}
        ]


def test_reader_csv_excel_1():
    """Тестируем выдачу ошибки о неподдерживаемом формате файла"""
    with pytest.raises(ValueError) as exc_info:
        reader_csv_excel("test.txt")
        assert str(exc_info.value) == "Неподдерживаемый формат файла."


def test_reader_csv_excel_2():
    """Тестируем выдачу ошибки при считывании файла"""
    with pytest.raises(Exception) as exc_info:
        reader_csv_excel("test_none.csv")
        assert str(exc_info.value) == "При считывании файла произошла ошибка."
