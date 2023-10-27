from src.masks import get_mask_card, returning_account_mask


def get_dict_cards_and_accounts(cards_and_accounts: str) -> dict:
    """Функция преобразовывает строку в словарь"""
    cards_and_accounts = cards_and_accounts.strip().split()
    name = ""
    dict_ = {}
    for word in cards_and_accounts:
        if word.isdigit():
            dict_[name] = word
            name = ""
        else:
            name += " " + word
    return dict_


def get_mask_cards_and_accounts(info: str) -> str:
    """Функция проверяет счет или карта и возврощает москированный список"""
    list_info = info.split()
    name = " ".join(list_info[:-1])
    number = list_info[-1]

    if "cчет" == name.islower():
        masked_info = (name + " " + returning_account_mask(number))
    else:
        masked_info = name + " " + get_mask_card(number)

    return masked_info


def get_data(datatime: str) -> str:
    """Функция возврощает дату"""
    get_data = datatime[8:10] + "." + datatime[5:7] + "." + datatime[0:4]
    return get_data
