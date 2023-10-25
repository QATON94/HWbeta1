from datetime import datetime, date, time
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

def get_data(time):
    get_time = time[8:10] + "." + time[5:7] + "." + time[0:4]
    return get_time