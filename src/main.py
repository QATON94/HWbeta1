def main():
    from src.masks import get_mask_card, returning_account_mask

    numbers_card = "7000792289606361"

    number_account = "73654108430135874305"

    numbers_card_dict = {
        "Maestro": 1596837868705199,
        "MasterCard": 7158300734726758,
        "Visa Classic": 6831982476737658,
        "Visa Platinum": 8990922113665229,
        "Visa Gold": 5999414228426353,
        }
    number_account_dict = {
        "Счет": 64686473678894779589,
        "Счет": 35383033474447895560,
        "Счет": 73654108430135874305
        }

    print(get_mask_card(numbers_card))
    print(returning_account_mask(number_account))


if __name__ == "__main__":
    main()
