def filter_by_currency(transactions: list[dict], currency: str):
    """Функция возврощает операцию заданной валюты
    :param transactions: Список словорей с транзакциями
    :param currency: Строка с названием волюты
    :yield: возвращает итератор, в которых указана заданная валюта.
    """
    for item in transactions:
        if currency == item["operationAmount"]["currency"]["name"]:
            yield item


def transaction_descriptions(transactions: list):
    """Функция возвращает описание каждой операции по очереди.
    :param transactions: Список словорей с транзакциями
    :yield: возвращает описание операции
    """
    for item in transactions:
        yield item["description"]


def card_number_generator(start: int, end: int):
    """Функция генерирует номера карт в формате "XXXX XXXX XXXX XXXX"
    :param start: Начало отсчета
    :param end: Конец отсчета
    :yield: возвращает сгенерированный номер карты
    """
    num = "0000000000000000"
    for number in range(start, end + 1):
        str_number = str(number)
        num = num[: -(len(str_number))] + str_number
        yield " ".join(num[i : i + 4] for i in range(0, len(num), 4))
