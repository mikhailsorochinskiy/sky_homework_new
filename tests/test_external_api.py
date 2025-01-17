from unittest.mock import patch

import pytest

from src.external_api import get_amount_transaction


@pytest.fixture
def operation_dict():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_get_amount_transaction_rub(operation_dict):
    assert get_amount_transaction(operation_dict) == "31957.58"


operation_dict_USD = {"operationAmount": {"amount": "319.58", "currency": {"name": "USD", "code": "USD"}}}


@patch("requests.request")
def test_get_amount_transaction_usd(mock_result):
    mock_result.return_value.json.return_value = {"result": 31958.00}
    assert get_amount_transaction(operation_dict_USD) == 31958.00
