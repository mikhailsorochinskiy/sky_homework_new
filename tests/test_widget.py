import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('card_number, expected',[('Visa Platinum 2202121234561234', 'Visa Platinum 2202 12** **** 1234'),
                                                  ('Maestro 2202121234561234', 'Maestro 2202 12** **** 1234'),
                                                  ('Счет 73654108430135874305', 'Счет **4305')])
def test_mask_account_card(card_number, expected):
    assert mask_account_card(card_number) == expected


def test_mask_account_card_not_correct_name():
    with pytest.raises(ValueError):
        mask_account_card('V 2202121234561234')
        mask_account_card('Ma 2202121234561234')
        mask_account_card('Сч 73654108430135874305')


def test_mask_account_card_not_correct_number():
    with pytest.raises(ValueError):
        mask_account_card('Visa Platinum 220212123456')
        mask_account_card('Maestro 220212123456')
        mask_account_card('Счет 736541084301358')


def test_mask_account_card_not_digit_number():
    with pytest.raises(ValueError):
        mask_account_card('Visa Platinum 22021212345612aa')
        mask_account_card('Maestro 22021212345612bb')
        mask_account_card('Счет 736541084301358743cc')


@pytest.fixture()
def date():
    return "11.03.2024"


def test_get_date(date):
    assert get_date('2024-03-11T02:26:18.671407') == date


def test_get_date_incorrect_format():
    with pytest.raises(ValueError):
        get_date('2024-03-11R02:26:18.671407')
        get_date('2024-03-11T02:26:18.')
        get_date('2024-03-11T02:26:18:671407')
        get_date('2024-03-11T02:26.18.671407')
        get_date('2024-03.11T02:26:18.671407')


def test_get_date_no_data():
    with pytest.raises(ValueError):
        get_date('T02:26:18.671407')
