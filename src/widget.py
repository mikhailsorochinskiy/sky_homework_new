from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """ Маскировка карты или счета"""
    new_card_number = ''
    if card_number.startswith("Visa Platinum"):
        new_card_number += "Visa Platinum "
        new_card_number += get_mask_card_number(card_number[14:])
    elif card_number.startswith("Maestro"):
        new_card_number += "Maestro "
        new_card_number += get_mask_card_number(card_number[8:])
    elif card_number.startswith("Счет"):
        new_card_number += "Счет "
        new_card_number += get_mask_account(card_number[5:])
    else:
        return "Введен неправильный номер или счет"
    return new_card_number


def get_date(operation_date: str) -> str:
    new_date_1 = operation_date.split("T")
    new_date_2 = new_date_1[0].split("-")
    return f'{new_date_2[-1]}.{new_date_2[-2]}.{new_date_2[-3]}'
