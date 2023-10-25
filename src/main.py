from src.widget import get_accounts_mask, get_mask_cards, get_data


def main():

    name_card = "Maestro"
    number_card = "1596837868705199"

    name_account = "Счет"
    number_account = "64686473678894779589"

    time = "2018-07-11T02:26:18.671407"

    print(get_mask_cards(name_card, number_card))
    print(get_accounts_mask(name_account, number_account))



    print(get_data(time))


if __name__ == "__main__":
    main()
