from datetime import datetime


def choice_state(list_dict: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Функция возврощает список словорей у которых ключ
    state содержит переданное в функцию значение
    """
    state_dict = []
    for dict_ in list_dict:
        if dict_["state"] == state:
            state_dict.append(dict_)

    return state_dict


def sort_date(list_dict: list[dict], reverse_: bool = True) -> list[dict]:
    """
    Функция сортировки списка операций по дате.
    :param list_dict: Список словарей для сортировки
    :param reverse_: Параметр направления сортировки. По-умолчанию - True
    :return: Отсортированный список операций по дате
    """
    sort_list = sorted(list_dict, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse_)
    return sort_list
