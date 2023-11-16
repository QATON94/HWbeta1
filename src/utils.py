import json
from typing import Any

import requests


def transaction_json(json_file_path: Any) -> list | dict:
    """Функция возврощается список транзакций или пустой список
    param path_: Путь к json файлу с транзакциями
    return: возврощает пустой список если файл не найден, либо список транзакций
    """
    try:
        with open(json_file_path, "r", encoding="UTF-8") as file:
            transactions = json.load(file)
        return transactions
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []


def transaction_amount(transaction):
    """Функция возврощает сумму транзакций в рублях, если не в рублях выводит ошибку
    :param transaction: Словарь с данными о транзакции
    :return сумма транзакции
    :raise Ошбика если транзакция не в рублях
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        cash_rate = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()["Valute"]
        name_code = transaction["operationAmount"]["currency"]["code"]
        value = cash_rate[name_code]['Value']
        amount_rate = round(float(value) * float(transaction["operationAmount"]["amount"]), 2)
        return amount_rate
