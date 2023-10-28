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
