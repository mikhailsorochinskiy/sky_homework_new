def get_mask_card_number(card_number: str) -> str:
    """Замена цифр с 7 по 12 элемент на '*', и разбиение по 4 цифры"""
    if len(card_number) != 16 or card_number.isdigit() is False:
        return "Введен неправильный номер карты"
    else:
        update_card_number = list(card_number)
        for i in range(6, 12):
            update_card_number[i] = "*"
        result_card_number = "".join(update_card_number)
        return " ".join(result_card_number[i: i + 4] for i in range(0, len(result_card_number), 4))


def get_mask_account(account_number: str) -> str:
    """Номер счета принимате вид: **XXXX (X - цифра)"""
    return "**" + account_number[-4:]
