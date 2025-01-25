import logging

logging.basicConfig(
    filename="../logs/masks.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    level=logging.DEBUG,
    encoding="utf-8",
)


logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: str) -> str:
    """Замена цифр с 7 по 12 элемент на '*', и разбиение по 4 цифры"""
    logger.info("Начало работы функции по маскировки номера карты")
    if len(card_number) != 16 or card_number.isdigit() is False:
        logger.error("Введено неправильный номер карты. Остановка программы")
        raise ValueError("Некорректное значение")
    update_card_number = list(card_number)
    for i in range(6, 12):
        update_card_number[i] = "*"
    result_card_number = "".join(update_card_number)
    logger.info("Номер карты замаскирован. Конец работы программы")
    return " ".join(result_card_number[i: i + 4] for i in range(0, len(result_card_number), 4))


def get_mask_account(account_number: str) -> str:
    """Номер счета принимает вид: **XXXX (X - цифра)"""
    logger.info("Начало работы функции по маскировки номера счета")
    if len(account_number) != 20 or account_number.isdigit() is False:
        logger.error("Введено неправильный номер счета. Остановка программы")
        raise ValueError("Некорректное значение")
    logger.info("Номер счета замаскирован. Конец работы программы")
    return "**" + account_number[-4:]
