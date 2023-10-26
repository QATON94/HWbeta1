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


def get_mask_cards_and_accounts(cards_and_accounts: str) -> str:
    """Функция проверяет счет или карта и возврощает москированный список"""
    dict_cards_and_accounts = get_dict_cards_and_accounts(cards_and_accounts)
    mask_cards_and_accounts = ""
    for name, number in dict_cards_and_accounts.items():
        if "cчет" == name.islower():
            mask_cards_and_accounts += (
                name + " " + returning_account_mask(number) + "\n"
            )
        else:
            mask_cards_and_accounts += name + " " + get_mask_card(number) + "\n"

    return mask_cards_and_accounts


def get_data(datatime: str) -> str:
    """Функция возврощает дату"""
    get_data = datatime[8:10] + "." + datatime[5:7] + "." + datatime[0:4]
    return get_data
