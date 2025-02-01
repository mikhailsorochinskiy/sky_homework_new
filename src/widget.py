from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Маскировка карты или счета"""
    new_card_number = ""
    split_card_number = card_number.split()
    if len(split_card_number[-1]) == 16 or len(split_card_number[-1]) == 20:
        if card_number.startswith("Счет"):
            new_card_number += "Счет "
            new_card_number += get_mask_account(card_number[5:])
        else:
            if len(split_card_number) == 2:
                new_card_number += split_card_number[0] + ' '
                new_card_number += get_mask_card_number(split_card_number[1])
            else:
                new_card_number += split_card_number[0] + ' ' + split_card_number[1] + ' '
                new_card_number += get_mask_card_number(split_card_number[2])
    else:
        raise ValueError("Некорректные данные")
    return new_card_number


def get_date(operation_date: Any) -> Any | None:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"("11.03.2024")"""
    if operation_date.startswith("T"):
        raise ValueError("Отсутствует дата")
    if operation_date[10] != "T":
        raise ValueError("Неправильный формат")
    if operation_date[13] != ":" or operation_date[16] != ":":
        raise ValueError("Неправильный формат времени")
    if operation_date[4] != "-" or operation_date[7] != "-":
        raise ValueError("Неправильный формат даты")
    new_date_1 = operation_date.split("T")
    new_date_2 = new_date_1[0].split("-")
    return f"{new_date_2[-1]}.{new_date_2[-2]}.{new_date_2[-3]}"
