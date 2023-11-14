import json
from typing import Any


def transaction_amount(json_file_path: Any) -> float | list:
    """Функция возврощается сумму рублевых транзакций
    param path_: Путь к json файлу с данными транзакций
    return: возврощает пустой список если файл не найден, либо сумму рублевых транзакций
    """
    try:
        with open(json_file_path, "r", encoding="UTF-8") as file:
            transactions = json.load(file)
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []

    if transactions == []:
        return []
    else:
        amount_sum = 0.0
        for transaction in transactions:
            try:
                if transaction["operationAmount"]["currency"]["code"] == "RUB":
                    value_amount = transaction["operationAmount"]["amount"]
                    amount_sum += float(value_amount)
            except ValueError:
                print("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
            except KeyError:
                print("Неверная сумма транзакции")
        return round(amount_sum, 2)
