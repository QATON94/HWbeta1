def get_mask_cards(numbers_card: dict) -> dict:
    """
    Функция возврощает информацию и маску номеров карт
    в формате: Имя Карты XXXX XX** **** XXXX
    """
    mask_card = {}
    for name_card, card in numbers_card:
        mask_card[name_card] = card[0:4] + " " + card[3:6] + "** **** " + card[-4:]

    return mask_card


def returning_accounts_mask(accounts_numbers: dict) -> dict:
    """Функция возврощает маску счетой в виде: **XXXX"""
    mask_account = {}
    for name_account, mask_account in accounts_numbers:
        mask_account[name_account] = "**" + mask_account[-4:]
    return mask_account
