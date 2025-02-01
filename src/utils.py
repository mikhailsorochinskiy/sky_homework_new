import json
import logging

logging.basicConfig(
    filename="C:/Users/Viktor/PycharmProjects/sky_homework_new/logs/utils.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    level=logging.DEBUG,
    encoding="utf-8",
)


logger = logging.getLogger(__name__)


def get_operations_from_json(file: str) -> list[dict]:
    """Функция принимает json-файл и возвращает список словарей о транзакциях"""
    logger.info("Начало работы программы по обработке json-файла")
    try:
        with open(file, encoding="utf-8") as f:
            operations = json.load(f)
        if type(operations) is not list:
            logger.warning("Программа вернула пустой список. Переданный аргумент не является списком")
            return []
        logger.info("Программа вернула список словарей о транзакциях и завершила свою работу")
        return operations
    except json.JSONDecodeError:
        logger.warning("Программа вернула пустой список. Ошибка JSONDecodeError")
        print(f"Ошибка декодирования JSON: {file}")
        return []
    except FileNotFoundError:
        logger.warning("Программа вернула пустой список. Ошибка FileNotFoundError")
        print(f"Файл {file} не найден")
        return []
