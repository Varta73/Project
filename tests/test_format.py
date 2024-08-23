from unittest.mock import mock_open, patch

import pytest

from src.format import reader_csv_excel


@patch("csv.reader")
def test_reader_file_transaction_csv(mock_reader):
    m = mock_open()
    mock_reader.return_value = [
        {"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z", "amount": "16210"}
    ]

    with patch("builtins.open", m) as mocked_open:
        assert reader_csv_excel("transaction.csv") == [
            {"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z", "amount": "16210"}
        ]

        mocked_open.assert_called_with("transaction.csv", "r", encoding="utf-8")


def test_reader_csv_excel_1():
    with pytest.raises(ValueError) as exc_info:
        reader_csv_excel("test.txt")
        assert str(exc_info.value) == "Неподдерживаемый формат файла."


def test_reader_csv_excel_2():
    with pytest.raises(Exception) as exc_info:
        reader_csv_excel("test_none.csv")
        assert str(exc_info.value) == "При считывании файла произошла ошибка."
