from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция принимает список словарей и возвращает те словари,
    в которых значения ключа state = EXECUTED"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], sort_option: bool = True) -> List[Dict[str, Any]]:
    """Функция сортирует список словарей по датам в порядке убывания"""
    return sorted(data, key=lambda x: x["date"], reverse=sort_option)
