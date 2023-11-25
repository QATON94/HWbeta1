from pathlib import Path
from pprint import pprint

from src.generators import (
    get_transactions_categories,
    get_values_operations,
    search_operations,
)
from src.logger import setup_logging
from src.utils import transaction_json

logger = setup_logging()


def main():
    logger.info(["Запуск программы..."])

    ROOT_PATH = Path(__file__).parent.parent
    OPERATIONS_JSON = ROOT_PATH.joinpath("data", "transactions_excel.xlsx")

    transactions = transaction_json(OPERATIONS_JSON)
    search_string = "Перевод организации"
    operations_categories = get_transactions_categories(transactions)
    print(get_transactions_categories(transactions))
    print(get_values_operations(transactions, operations_categories))
    pprint(search_operations(transactions, search_string))

    # if transactions != []:
    #     result = transaction_amount(transactions[0])
    #     print(result)
    #     card = get_mask_cards_and_accounts(transactions[0]["from"])
    #     account_number = get_mask_cards_and_accounts(transactions[0]["to"])
    #     print(card)
    #     print(account_number)
    #
    logger.info(["Завершение программы..."])


if __name__ == "__main__":
    main()
