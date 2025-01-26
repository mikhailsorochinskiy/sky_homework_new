from unittest.mock import patch

import pytest

from src.csv_excel import get_transactions_from_csv, get_transactions_from_excel

transactions = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
]


@patch("pandas.read_csv")
def test_get_transactions_from_csv(mock_reader):
    mock_reader.return_value.to_dict.return_value = transactions
    assert get_transactions_from_csv("transactions.csv") == transactions


@patch("pandas.read_excel")
def test_get_transactions_from_excel(mock_reader):
    mock_reader.return_value.to_dict.return_value = transactions
    assert get_transactions_from_excel("transactions_excel.xlsx") == transactions


def test_get_transactions_from_csv_negative():
    with pytest.raises(FileNotFoundError):
        get_transactions_from_csv("invalid_path")


def test_get_transactions_from_excel_negative():
    with pytest.raises(FileNotFoundError):
        get_transactions_from_excel("invalid_path")
