import json


def get_operations_from_json(file: str) -> list[dict]:
    """Функция принимает json-файл и возвращает список словарей о транзакциях"""
    try:
        with open(file, encoding="utf-8") as f:
            operations = json.load(f)
        if type(operations) is not list:
            return []
        return operations
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON: {file}")
        return []
    except FileNotFoundError:
        print(f"Файл {file} не найден")
        return []
