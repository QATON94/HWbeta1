import pytest

from src.utils import transaction_amount


@pytest.mark.parametrize("transaction, expected", [("transaction_test1.json", 31957.58),
                                                   ("transaction_test2.json", [])])
def test_transaction_amount(transaction, expected):
    amount = transaction_amount(transaction)
    assert amount == expected
