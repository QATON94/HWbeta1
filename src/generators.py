import re
from collections import Counter
from typing import Any


def filter_by_currency(transactions: list[dict], currency: str) -> Any:
    """Функция возврощает операцию заданной валюты
    :param transactions: Список словорей с транзакциями
    :param currency: Строка с названием волюты
    :yield: возвращает итератор, в которых указана заданная валюта.
    """
    for item in transactions:
        if currency == item["operationAmount"]["currency"]["name"]:
            yield item


def transaction_descriptions(transactions: list) -> Any:
    """Функция возвращает описание каждой операции по очереди.
    :param transactions: Список словорей с транзакциями
    :yield: возвращает описание операции
    """
    for item in transactions:
        yield item["description"]


def card_number_generator(start: int, end: int) -> Any:
    """Функция генерирует номера карт в формате "XXXX XXXX XXXX XXXX"
    :param start: Начало отсчета
    :param end: Конец отсчета
    :yield: возвращает сгенерированный номер карты
    """
    num = "0000000000000000"
    for number in range(start, end + 1):
        str_number = str(number)
        num = num[: -(len(str_number))] + str_number
        yield " ".join(num[i: i + 4] for i in range(0, len(num), 4))


def search_operations(transactions: list[dict], search_string: str) -> list[dict]:
    """Функция принимает список словарей и возврощает список словарей в которых есть значение search_string
    :param transactions: Список словорей с транзакциями
    :param search_string: Слово поиска по операциям
    :return: возврощает список словарей
    """
    operations_list = []
    for item in transactions:
        try:
            if re.search(search_string, item["description"]):
                operations_list.append(item)
        except TypeError:
            continue

    return operations_list


def get_transactions_categories(transactions: list) -> dict:
    """Функция принимает список словарей с транзакциями и возврощает словарь с категориями операций"""
    transactions_categories = {}
    for row in transactions:
            transactions_categories[row['description']] = 0
    return transactions_categories


def get_values_operations(transactions: list, operations_categories: dict) -> dict:
    """
    :param transactions: список славарей с транзакциями
    :param operations_categories: словарь с категориями операций
    ;:return возврощает словарь скаличеством операций в каждой категории
    """
    for row in transactions:
        if row['description'] in operations_categories.keys():
            operations_categories[row['description']] += 1
    count = Counter(operations_categories)
    return count
