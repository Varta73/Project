import json
from typing import Any
import json
from typing import Any

def get_transaction(file_json: str) -> Any:
    """
    Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.

    """

    with open(file_json, encoding="utf-8") as f:
        try:
            trans = json.load(f)
            return trans

        except:
            return []


print(
    json.dumps(
        get_transaction(r"C:\Users\Светлана\PycharmProjects\pythonProject\data\operations.json"),
        indent=4,
    )
)
