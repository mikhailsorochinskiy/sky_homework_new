import json
import os


def get_operations_from_json(file: str) -> list[dict]:
    """Функция принимает json-файл и возвращает список словарей о транзакциях"""
    if not os.path.isfile(file):
        print(f"Файл не найден: {file}")
        return []
    with open(file, encoding="utf-8") as f:
        operations = json.load(f)
    if type(operations) is not list:
        return []
    return operations
