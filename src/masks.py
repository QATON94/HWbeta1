def get_mask_card(number_card: str) -> str:
    """
    Функция возврощает маску номера карты
    в формате XXXX XX** **** XXXX
    """
    mask_card = number_card[0:4] + " " + number_card[3:6] + "** **** " + number_card[-4:]
    return mask_card


def returning_account_mask(account_mask: str) -> str:
    """Функция возврощает маску счета в виде **XXXX"""
    mask_account = "**" + account_mask[-4:]
    return mask_account
