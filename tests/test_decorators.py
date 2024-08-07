import tempfile

from src.decorators import log

from typing import Any


def test_log_good(capsys: Any) -> Any:
    """Тестирует выполнение декорированной функции"""

    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    result = my_function(1, 2)

    assert result == 3


def test_log_good_file_log(capsys: Any) -> Any:
    """Тестирует запись в файл после успешного выполнения"""

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert "my_function ok" in logs


def test_log_exception(capsys: Any) -> Any:
    """Тестирует вывод после ошибки в консоль"""

    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, "2")

    captured = capsys.readouterr()

    assert "my_function error" in captured.out


def test_log_exception_file_log(capsys: Any) -> Any:
    """Тестирует запись в файл после ошибки"""

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, "2")

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert "my_function error" in logs
