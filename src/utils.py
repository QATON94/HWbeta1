import csv
import json
import logging
import os
from typing import Any, Union

import pandas as pd
import requests
from pandas import DataFrame

logger = logging.getLogger(__name__)


def transaction_json(file_path: Any) -> Union[list[Any] | dict[Any, Any]]:
    """Функция возврощается список транзакций или пустой список
    param path_: Путь к json файлу с транзакциями
    return: возвращает пустой список если файл не найден, либо список транзакций
    """
    file_name, file_extension = os.path.splitext(file_path)
    print(file_extension)
    transactions = []
    try:
        logger.info(f"Открывается файл: {file_path}")
        with open(file_path, "r", encoding="UTF-8") as file:
            if file_extension == ".json":
                transactions = json.load(file)
            elif file_extension == ".csv":
                transactions_file = csv.DictReader(file, delimiter=";")
                for row in transactions_file:
                    transactions.append(row)
                transactions = conv_csv(transactions)
            elif file_extension == ".xlsx":
                transactions_reader: DataFrame = pd.read_excel(file_path)
                print(transactions)
                transactions = conv_xlsx(transactions_reader)

        return transactions
    except FileNotFoundError:
        logger.error("Файл не найден FileNotFoundError")
        return transactions
    except json.JSONDecodeError:
        logger.error("файл JSON не соответствуют правильному формату: FileNotFoundError")
        return transactions


def transaction_amount(transaction: Any) -> float:
    """Функция возврощает сумму транзакций в рублях, если не в рублях выводит ошибку или конвертирует
    :param transaction: Словарь с данными о транзакции
    :return сумма транзакции
    :raise Ошибика если транзакция не в рублях
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount_rate = float(transaction["operationAmount"]["amount"])
        logger.info(f"Сумма транзакции: {amount_rate}")
        return float(transaction["operationAmount"]["amount"])
    else:
        cash_rate = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()["Valute"]
        name_code = transaction["operationAmount"]["currency"]["code"]
        print(name_code)
        logger.info(f"Получаем информацию курса {name_code}")
        value = cash_rate[name_code]["Value"]
        amount_rate = round(float(value) * float(transaction["operationAmount"]["amount"]), 2)
        logger.info(f"Сумма транзакции: {amount_rate}")
        return amount_rate


def conv_csv(csv_: list[Any]) -> list[Any]:
    """Функция получает список вида csv, возвращает измененный список словарей в вида JSON"""
    conv_list = []
    for list_ in csv_:
        list_["operationAmount"] = {}
        list_["operationAmount"]["amount"] = list_.pop("amount")
        list_["operationAmount"]["currency"] = {}
        list_["operationAmount"]["currency"]["name"] = list_.pop("currency_name")
        list_["operationAmount"]["currency"]["code"] = list_.pop("currency_code")
        conv_list.append(list_)
    return conv_list


def conv_xlsx(xslx_: Any) -> list[dict[str, dict[str, dict]]]:
    """Функция получает список вида xlsx, возвращает измененный список словарей в вида JSON"""
    num_rows = xslx_.shape[0]
    print(num_rows)
    transactions_list_dict = []
    for i in range(0, num_rows):
        transactions_dict: dict[str, dict[str, dict[Any, Any]] | Any] = {
            "operationAmount": {"currency": {}},
            "id": xslx_.iloc[i, 0],
            "state": xslx_.iloc[i, 1],
            "date": xslx_.iloc[i, 2],
        }
        transactions_dict["operationAmount"]["amount"] = xslx_.iloc[i, 3]
        transactions_dict["operationAmount"]["currency"]["name"] = xslx_.iloc[i, 4]
        transactions_dict["operationAmount"]["currency"]["code"] = xslx_.iloc[i, 5]
        transactions_dict["description"] = xslx_.iloc[i, 8]
        transactions_dict["from"] = xslx_.iloc[i, 6]
        transactions_dict["to"] = xslx_.iloc[i, 7]
        transactions_list_dict.append(transactions_dict)

    return transactions_list_dict
