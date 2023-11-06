from src.generators import filter_by_currency, transaction_descriptions
import json


def main() -> None:
    with open('C:/Payton_training/HWbeta1/data/transactions.json', 'r', encoding="UTF-8") as file:
        transactions = json.load(file)

    usd_transactions = filter_by_currency(transactions, "USD")

    for _ in range(2):
        print(next(usd_transactions)["id"])

    descriptions = transaction_descriptions(transactions)

    for _ in range(5):
        print(next(descriptions))



if __name__ == "__main__":
    main()
