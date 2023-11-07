import json
import os

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def main() -> None:
    with open(os.path.join("..", "data", "transactions.json"), "r", encoding="UTF-8") as file:
        transactions = json.load(file)

    usd_transactions = filter_by_currency(transactions, "руб.")

    for _ in range(2):
        print(next(usd_transactions)["id"])

    descriptions = transaction_descriptions(transactions)

    for _ in range(5):
        print(next(descriptions))

    for card_number in card_number_generator(1, 5):
        print(card_number)


if __name__ == "__main__":
    main()
