import re
from collections import Counter


def get_list_with_main_string(transactions: list[dict], text: str) -> list[dict]:
    """Функция принимает список транзакций и искомый текст и возвращает список, в которых
    есть заданный текст"""
    result_list = [transaction for transaction in transactions
                   if re.search(f'{text}', str(transaction), flags=re.IGNORECASE)]
    return result_list


def get_counter_type_operation(transactions: list[dict], types: list) -> dict:
    """Функция принимает список транзакций и список типов операций и возвращает словарь о количестве каждой операции"""
    list_types = [transaction.get("description") for transaction in transactions
                  if transaction.get("description") is not None]
    counter_types = Counter(list_types)
    dict_types = dict()
    for item in types:
        if dict(counter_types).get(item) is not None:
            dict_types[item] = dict(counter_types).get(item)
        else:
            dict_types[item] = 0
    return dict_types
