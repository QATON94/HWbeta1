def filter_by_currency(transactions:list, currency:str) -> int:

    for item in transactions:
        if currency == item['operationAmount']["currency"]["name"]:
            yield item


def transaction_descriptions(transactions:list):
    for item in transactions:
        yield item["description"]


def card_number_generator(start, end):
    num = '0000000000000000'
    for number in range(start, end+1):
        number = str(number)
        num = num[:-(len(number))] + number
        yield ' '.join(num[i:i+4] for i in range(0, len(num), 4))
