import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


transactions = {
    "id": 207126257,
    "state": "EXECUTED",
    "date": "2019-07-15T11:47:40.496961",
    "operationAmount": {"amount": "92688.46", "currency": {"name": "USD", "code": "USD"}},
    "description": "Открытие вклада",
    "to": "Счет 35737585785074382265",
}


def convert_transactions_amount(transactions: dict) -> float | str:
    """Функция принимает значение в долларах, обращается к API и возвращает конвертацию в рубли/"""
    amount = transactions["operationAmount"].get("amount")
    currency = transactions["operationAmount"]["currency"].get("code")
    if currency == "RUB":
        return float(amount)
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.request("GET", url, headers=headers)
        result = response.json()
        return float(result["result"])
    return float(amount)


print(convert_transactions_amount(transactions))
