def main():
    from src.masks import get_mask_card, returning_account_mask

    numbers_card = "7000792289606361"
    number_account = "73654108430135874305"

    print(get_mask_card(numbers_card))
    print(returning_account_mask(number_account))


if __name__ == "__main__":
    main()
