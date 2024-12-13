def filter_by_state(id_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает те словари,
    в которых значения ключа state = EXECUTED"""
    new_id_list = []
    for items in id_list:
        if items["state"] == state:
            new_id_list.append(items)

    return new_id_list
