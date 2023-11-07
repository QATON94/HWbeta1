import json
import os

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.fixture()
def transaction():
    with open(os.path.join("..", "data", "transactions.json"), "r", encoding="UTF-8") as file:
        transactions = json.load(file)
    return transactions


@pytest.mark.parametrize("currency, expected", [("USD", [939719570, 142264268]), ("руб.", [873106923, 594226727])])
def test_filter_by_currency(transaction, currency, expected):
    for _ in range(2):
        usd_transactions = filter_by_currency(transaction, currency)
        assert (next(usd_transactions)["id"]) == expected[0]
        assert (next(usd_transactions)["id"]) == expected[1]


@pytest.mark.parametrize(
    "expected",
    [
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ]
    ],
)
def test_transaction_descriptions(transaction, expected):
    descriptions = transaction_descriptions(transaction)
    assert list(descriptions) == list(expected)


def test_card_number_generator():
    assert next(card_number_generator(5, 5)) == "0000 0000 0000 0005"
