from unittest.mock import Mock

from src.utils import get_transaction
from typing import Any

def test_get_transaction()-> Any:
    """Функция тестирует возврат пустого списка, если на входе список пуст"""
    mock_get_transaction = Mock(return_value=[])
    trans = mock_get_transaction
    assert get_transaction(trans) == []
    mock_get_transaction.assert_called_once_with(file_json=[])
