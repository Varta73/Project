from typing import Any, Iterable

# state = [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#     ]


def filter_by_state(
    states: list[dict[str, Any | None]], stat_id: str = "EXECUTED"
) -> list[dict[str, Any | None]] | bool:
    """Функция сортировки по ключу state"""
    new_state = []
    for key in states:
        if key.get("state") == stat_id:
            new_state.append(key)
    return new_state


# print(filter_by_state(state))


def sort_by_date(state: Iterable[Any], reverse: bool = True) -> Iterable[Any | bool]:
    """Функция сортировки по дате"""
    sorted_date = sorted(state, key=lambda state: state.get("date"), reverse=reverse)
    return sorted_date


# print(sort_by_date(state))
