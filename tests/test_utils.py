from pathlib import Path
from unittest.mock import patch

import pytest

from src.utils import transaction_amount, transaction_json

ROOT_PATH = Path(__file__).parent.parent


@pytest.fixture()
def transaction_1():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


@pytest.fixture()
def transaction_2():
    return ({
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
    )


@pytest.fixture()
def transaction_csv():
    return [{'id': '441945886', 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
             'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589',
             'description': 'Перевод организации',
             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}}]


@pytest.fixture()
def transaction_xlsx():
    return [{'operationAmount': {'currency': {'name': 'руб.', 'code': 'RUB'}, 'amount': 31957.58}, 'id': 441945886,
             'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'description': 'Перевод организации',
             'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}]


@pytest.fixture()
def path1():
    test_operations_json1 = ROOT_PATH.joinpath("data", "transaction_test1.json")
    return test_operations_json1


@pytest.fixture()
def path2():
    test_operations_json2 = ROOT_PATH.joinpath("data", "transaction_test2.json")
    return test_operations_json2


@pytest.fixture()
def path_csv():
    test_operations_json3 = ROOT_PATH.joinpath("data", "test_csv.csv")
    return (test_operations_json3)


@pytest.fixture()
def path_xlsx():
    test_operations_json4 = ROOT_PATH.joinpath("data", "test_excel.xlsx")
    return test_operations_json4


def test_transaction_json(path1, path2, transaction_1):
    amount1 = transaction_json(path1)
    amount2 = transaction_json(path2)
    amount3 = transaction_json(" ")

    assert amount1 == transaction_1
    assert amount2 == []
    assert amount3 == []


def test_transaction_json_open_csv(path_csv, transaction_csv):
    amount = transaction_json(path_csv)
    assert amount == transaction_csv


def test_transaction_json_open_xlsx(path_xlsx, transaction_xlsx):
    amount = transaction_json(path_xlsx)
    assert amount == transaction_xlsx


def test_transaction_amount(transaction_1):
    assert transaction_amount(transaction_1) == 31957.58


def test_transaction_usd_amount(transaction_2):
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'Valute': {
            "USD": {'ID': 'R01235', 'NumCode': '840', 'CharCode': 'USD', 'Nominal': 1, 'Name': 'Доллар США',
                    'Value': 88.9466, 'Previous': 89.4565}}}
        assert transaction_amount(transaction_2) == 731262.91
        mock_get.assert_called_once_with('https://www.cbr-xml-daily.ru/daily_json.js')

# def test_error_transaction_amount(transaction_2):
#     with pytest.raises(ValueError):
#         transaction_amount(transaction_2)
