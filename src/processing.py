from datetime import datetime


def choice_state(list_dict: list, state: str) -> list:
    """
    Функция возврощает список словорей у которых ключ
    state содержит переданное в функцию значение
    """
    state_dict = []
    for dict_ in list_dict:
        if dict_["state"] == state:
            state_dict.append(dict_)

    return state_dict


def sort_date(list_dict: list, reverse_: bool = True) -> list:
    """Функция возврощает отсортированный словарь по дате"""
    sort_list = sorted(list_dict, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse_)
    return sort_list
