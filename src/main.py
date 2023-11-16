from pathlib import Path

from src.utils import transaction_amount, transaction_json


def main() -> None:
    ROOT_PATH = Path(__file__).parent.parent
    OPERATIONS_JSON = ROOT_PATH.joinpath("data", "operations.json")
    # with open(os.path.join("..", "data", "transactions.json"), "r", encoding="UTF-8") as file:
    #     transactions = json.load(file)
    #
    # usd_transactions = filter_by_currency(transactions, "руб.")
    #
    # for _ in range(2):
    #     print(next(usd_transactions)["id"])
    #
    # descriptions = transaction_descriptions(transactions)
    #
    # for _ in range(5):
    #     print(next(descriptions))
    #
    # for card_number in card_number_generator(1, 5):
    #     print(card_number)

    transactions = transaction_json(OPERATIONS_JSON)
    print(transaction_amount(transactions[0]))


if __name__ == "__main__":
    main()
