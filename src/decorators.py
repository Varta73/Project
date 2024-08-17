from typing import Any, Callable

def log(filename=None) -> Callable:
    """Декоратор логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def decorator(my_function: Any) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if not filename:
                try:
                    result = my_function(*args, **kwargs)
                    print(
                        f"{my_function.__name__} Начало работы \n "
                        f"Результат: {result} \n {my_function.__name__} ok \n {my_function.__name__} Конец работы"
                    )
                except Exception as e:
                    print(
                        f"{my_function.__name__} \n "
                        f"Тип ошибки: {e}. \n Данные, вызвавшие ошибку: {args}, {kwargs}"
                    )
            else:
                try:
                    result = my_function(*args, **kwargs)
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(
                            f"{my_function.__name__} Начало работы \n "
                            f"Результат: {result} \n {my_function.__name__} ok \n {my_function.__name__} Конец работы"
                        )
                except Exception as e:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(
                            f"{my_function.__name__} \n Тип ошибки: {e}. \n Данные, вызвавшие ошибку: {args}, {kwargs}"
                        )

        return wrapper

    return decorator


@log("file_log")
def my_function(x: int, y: int) -> int:
    return x + y


# my_function(2, 3)

my_function(1, "t")

# my_function("3", "2")
