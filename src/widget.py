from src.masks import get_mask_account
from datetime import datetime

def mask_account_card():


def get_data(data: str) -> str:
    """Функция принимает на вход данные о дате и времени и возвращает строку с датой в формате
"ДД.ММ.ГГГГ"""
    dat = datetime.strptime(data, format("%Y-%m-%dT%H:%M:%S.%f"))
    return (dat.strftime("%d.%m.%Y"))

print (get_data("2024-07-22T02:26:18.671407"))


