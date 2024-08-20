from unittest.mock import patch

from src.external_api import convert_transactions_amount, transactions


@patch("requests.get")
def test_convert_transactions_amount(mock_get):

    mock_get.return_value.json.return_value = {"rates": {"RUB": 87.39642}}
    assert convert_transactions_amount(transactions) == 8292157.665919
