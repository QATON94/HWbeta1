import json
import logging
from typing import Any, Union

import requests

logger = logging.getLogger(__name__)


def transaction_json(json_file_path: Any) -> Union[list[Any] | dict[Any, Any]]:
    """Функция возврощается список транзакций или пустой список
    param path_: Путь к json файлу с транзакциями
    return: возврощает пустой список если файл не найден, либо список транзакций
    """
    try:
        logger.info(f"Открывается файл: {json_file_path}")
        with open(json_file_path, "r", encoding="UTF-8") as file:
            transactions = json.load(file)
        return transactions
    except FileNotFoundError:
        logger.error("Файл не найден FileNotFoundError")
        return []
    except json.JSONDecodeError:
        logger.error("файл JSON не соответствуют правильному формату: FileNotFoundError")
        return []


def transaction_amount(transaction: Any) -> float:
    """Функция возврощает сумму транзакций в рублях, если не в рублях выводит ошибку
    :param transaction: Словарь с данными о транзакции
    :return сумма транзакции
    :raise Ошбика если транзакция не в рублях
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount_rate = float(transaction["operationAmount"]["amount"])
        logger.info(f"Сумма транзакции: {amount_rate}")
        return float(transaction["operationAmount"]["amount"])
    else:

        cash_rate = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()["Valute"]
        name_code = transaction["operationAmount"]["currency"]["code"]
        logger.info(f"Получаем информацию курса {name_code}")
        value = cash_rate[name_code]['Value']
        amount_rate = round(float(value) * float(transaction["operationAmount"]["amount"]), 2)
        logger.info(f"Сумма транзакции: {amount_rate}")
        return amount_rate
