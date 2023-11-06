def filter_by_currency(transactions:list, currency):
    for item in transactions:
        if currency == item['operationAmount']["currency"]["name"]:
            yield item
