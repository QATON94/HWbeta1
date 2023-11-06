import json

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.fixture()
def transaction():
    with open("C:/Payton_training/HWbeta1/data/transactions.json", "r", encoding="UTF-8") as file:
        transactions = json.load(file)
    return transactions


@pytest.mark.parametrize("currency, expected", [("USD", 939719570), ("руб.", 873106923)])
def test_filter_by_currency(transaction, currency, expected):
    for _ in range(2):
        usd_transactions = filter_by_currency(transaction, currency)
        assert (next(usd_transactions)["id"]) == expected


def test_transaction_descriptions(transaction):
    descriptions = transaction_descriptions(transaction)
    assert next(descriptions) == "Перевод организации"


def test_card_number_generator():
    assert next(card_number_generator(5, 5)) == "0000 0000 0000 0005"
