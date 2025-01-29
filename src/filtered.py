import re
from collections import Counter

from src.utils import get_operations_from_json


def get_list_with_main_string(transactions: list[dict], text: str) -> list[dict]:
    """Функция принимает список транзакций и искомый текст и возвращает список, в которых
    есть заданный текст"""
    pattern = re.compile(f'{text}')
    result_list = [transaction for transaction in transactions if re.search(pattern, str(transaction))]
    return result_list


def get_counter_type_operation(transactions: list[dict], types: list) -> dict:
    list_types = [transaction.get("description") for transaction in transactions if transaction.get("description") is not None]
    counter_types = Counter(list_types)
    dict_types = dict()
    for item in types:
        if dict(counter_types).get(item) is not None:
            dict_types[item] = dict(counter_types).get(item)
        else:
            dict_types[item] = 0
    return dict_types
