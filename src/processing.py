def filter_by_state(id_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает те словари,
    в которых значения ключа state = EXECUTED"""
    new_id_list = []
    for items in id_list:
        if items["state"] == state:
            new_id_list.append(items)

    return new_id_list


def sort_by_date(id_list: list, sort_option: bool = True) -> list:
    """Функция сортирует список словарей по датам в порядке убывания"""
    return sorted(id_list, key=lambda x: x["date"], reverse=sort_option)
