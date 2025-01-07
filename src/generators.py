from typing import Any, Dict, Iterator, List


def filter_by_currency(operations: List[Dict[Any, Any]], currency: str) -> Iterator[Any]:
    """Функция принимает на вход список словарей, представляющих транзакции. Функция должна возвращать итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)
    """
    return filter(lambda x: x.get("operationAmount").get("currency").get("name") == currency, operations)


def transaction_descriptions(operations: List[Dict[str, Any]]) -> Iterator:
    """Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    if not operations:
        return
    for x in operations:
        yield x.get("description")


def card_number_generator(start: int, end: int) -> Iterator:
    """Генератор card_number_generator, который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать номера
    карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    if start > end or len(str(start)) > 16 or len(str(end)) > 16:
        start = False
        end = False
    if not start and not end:
        return
    for i in range(start, end + 1):
        zeros_len = 16 - len(str(i))
        card = "0" * zeros_len
        card += str(i)
        yield " ".join(card[i: i + 4] for i in range(0, len(card), 4))
        i += 1
