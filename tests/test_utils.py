from unittest.mock import mock_open, patch

from src.utils import get_operations_from_json

operations_test = """[{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }
  }
]
"""

mocked_open = mock_open(read_data=operations_test)


def test_get_operations_from_json():
    """ Положительный тест"""
    with patch('builtins.open', mocked_open):
        result = get_operations_from_json('../data/operations.json')
        assert get_operations_from_json('../data/operations.json') == result


def test_get_operations_from_json_invalid_path():
    """Тест с неправильным путем к файлу(отсутствие такого файла)"""
    assert get_operations_from_json("invalid_path") == []


def test_get_operations_from_json_not_list():
    """Файл empty.json пустой файл, то есть тип данных None, а не List"""
    assert get_operations_from_json("../data/empty.json") == []


invalid_json = """[{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }
"""


mocked_open_invalid_json = mock_open(read_data=invalid_json)


def test_get_operations_from_invalid_json():
    with patch('builtins.open', mocked_open_invalid_json):
        result = get_operations_from_json('../data/operations.json')
        assert get_operations_from_json('../data/operations.json') == result
