from src.widget import get_accounts_mask


def main():
    from src.masks import get_mask_card, returning_account_mask
    from src.widget import get_mask_cards
    name_card = "Maestro"
    number_card = "1596837868705199"

    name_account = "Счет"
    number_account = "64686473678894779589"

    # print(get_mask_card(numbers_card))
    # print(returning_account_mask(number_account))
    print(get_mask_cards(name_card, number_card))
    print(get_accounts_mask(name_account, number_account))


if __name__ == "__main__":
    main()
