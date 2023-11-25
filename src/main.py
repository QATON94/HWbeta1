from pathlib import Path
from pprint import pprint

from src.logger import setup_logging
from src.utils import transaction_amount, transaction_json
from src.widget import get_mask_cards_and_accounts

logger = setup_logging()


def main():
    logger.info(["Запуск программы..."])

    ROOT_PATH = Path(__file__).parent.parent
    OPERATIONS_JSON = ROOT_PATH.joinpath("data", "test_excel.xlsx")

    transactions = transaction_json(OPERATIONS_JSON)
    pprint(transactions)
    if transactions != []:
        result = transaction_amount(transactions[0])
        print(result)
        card = get_mask_cards_and_accounts(transactions[0]["from"])
        account_number = get_mask_cards_and_accounts(transactions[0]["to"])
        print(card)
        print(account_number)

    logger.info(["Завершение программы..."])


if __name__ == "__main__":
    main()
