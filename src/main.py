from src.widget import get_data, get_mask_cards_and_accounts


def main():
    datatime = "2018-07-11T02:26:18.671407"

    cards_and_accounts = """Maestro 1596837868705199"""
    # Счет 64686473678894779589
    # MasterCard 7158300734726758
    # Счет 35383033474447895560
    # Visa Classic 6831982476737658
    # Visa Platinum 8990922113665229
    # Visa Gold 5999414228426353
    # Счет 73654108430135874305"""

    print(get_mask_cards_and_accounts(cards_and_accounts))
    print(get_data(datatime))


if __name__ == "__main__":
    main()
