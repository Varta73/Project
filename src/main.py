from src.filter_transactions import get_filter_transaction_description
from src.format import reader_csv_excel
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transaction
from src.widget import get_data, mask_account_card


def main() -> None:
    """Функция, определяющая работу с конечным пользователем разработанной программы.
    Задаёт вопросы и в соответствии с полученными ответами работает с разработанными модулями."""
    # global direction, date_sorted_transactions, rub_transactions, result_transactions
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями!
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла;
    2. Получить информацию о транзакциях из CSV-файла;
    3. Получить информацию о транзакциях из XLSX-файла."""
    )
    """Выбор файла"""
    while True:
        user_input = input("Ваш выбор: ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")
    menu = {
        "1": "Для обработки выбран JSON-файл.",
        "2": "Для обработки выбран CSV-файл.",
        "3": "Для обработки выбран XLSX-файл.",
    }
    print(f"{menu[user_input]}")
    if user_input == "1":
        transactions = get_transaction("../data/operations.json")
    elif user_input == "2":
        transactions = reader_csv_excel("../data/transactions.csv")
    elif user_input == "3":
        transactions = reader_csv_excel("../data/transactions_excel.xlsx")

    """Фильтрация по статусу"""
    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        users_status = input("Введите выбранный статус: ").upper()
        if users_status in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")
    filtered_transaction = filter_by_state(transactions, users_status)
    print(f"Операции отфильтрованы по статусу {users_status}.")

    """Фильтрация по дате"""
    while True:
        print("Отфильтровать операции по дате?")
        users_date_sort = input("Введите да/нет: ").lower()
        if users_date_sort in ("да", "нет"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")
    if users_date_sort == "да":
        while True:
            print("Отфильтровать по возрастанию /по убыванию?")
            users_sort_direction = input("Ваш выбор: ").lower()
            if users_sort_direction in ("по возрастанию", "по убыванию"):
                break
            print("Введён некорректный ответ. Повторите ввод ответа.")
        if users_sort_direction == "по возрастанию":
            direction = False
        elif users_sort_direction == "по убыванию":
            direction = True
        date_sorted_transactions = sort_by_date(filtered_transaction, direction)
    elif users_date_sort == "нет":
        date_sorted_transactions = filtered_transaction

    """Фильтрация по валюте"""
    while True:
        print("Выводить только рублёвые транзакции?")
        currency_selection = input("Введите да/нет: ").lower()
        if currency_selection in ("да", "нет"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")
    if currency_selection == "да":
        rub_transactions = [
            transaction for transaction in date_sorted_transactions if transaction["currency_code"] == "RUB"
        ]
    elif currency_selection == "нет":
        rub_transactions = date_sorted_transactions

    """Фильтрация по определённому слову в описании"""
    while True:
        print("Отфильтровать список по определённому слову в описании?")
        selection_word = input("Введите да/нет: ").lower()
        if selection_word in ("да", "нет"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")
    if selection_word == "да":
        users_word_filter = input("Введите слово для сортировки: ").lower()
        result_transactions = get_filter_transaction_description(rub_transactions, users_word_filter)

    elif selection_word == "нет":
        result_transactions = rub_transactions

    """Вывод результатов"""
    count_of_transactions = len(result_transactions)
    if count_of_transactions > 0:
        print("Итоговый список транзакций")
        print(f"Всего банковских операций в выборке: {count_of_transactions}.\n")
        for item in result_transactions:
            if item["description"] == "Открытие вклада":
                print(
                    f"""Дата:{get_data(item["date"])}\n Операция:{item["description"]}
        Сумма: {item["amount"]} {item["currency_code"]}\n"""
                )
            else:
                print(
                    f"""Дата:{get_data(item["date"])}\n Операция:{item["description"]}
        {mask_account_card(item["from"])} -> {mask_account_card(item["to"])}
        Сумма: {item["amount"]} {item["currency_code"]}\n"""
                )
            # Вывод результата с пустым списком
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
