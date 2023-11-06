def filter_by_currency(transactions:list, currency):
    for item in transactions:
        if currency == item['operationAmount']["currency"]["name"]:
            yield item


def transaction_descriptions(transactions:list):
    for item in transactions:
        yield item["description"]