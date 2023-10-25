def get_mask_cards(name_card: str, number_card: str):
    """
    Функция возврощает информацию и маску номеров карт
    в формате: Имя Карты XXXX XX** **** XXXX
    """
    mask_card = name_card + " " + number_card[0:4] + " " + number_card[3:6] + "** **** " + number_card[-4:]
    return mask_card


def get_accounts_mask(name_account: str, number_account: str) -> str:
    """Функция возврощает маску счетой в виде: **XXXX"""

    mask_account = name_account + " **" + number_account[-4:]
    return mask_account


def get_data(datatime: str) -> str:
    """Функция возврощает дату"""
    get_data = datatime[8:10] + "." + datatime[5:7] + "." + datatime[0:4]
    return get_data
