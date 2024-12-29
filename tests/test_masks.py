import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture()
def card_number():
    return '2202 12** **** 1234'


def test_get_mask_card_number(card_number):
    assert get_mask_card_number('2202121234561234') == card_number


def test_get_mask_card_number_invalid_len():
    with pytest.raises(ValueError):
        get_mask_card_number('220212123')


def test_get_mask_card_number_not_is_digit():
    with pytest.raises(ValueError):
        get_mask_card_number('22021212345612aa')


@pytest.fixture()
def account_number():
    return '**4305'


def test_get_mask_account(account_number):
    assert get_mask_account('73654108430135874305') == account_number


def test_get_mask_account_number_invalid_len():
    with pytest.raises(ValueError):
        get_mask_account('567890')


def test_get_mask_account_number_not_is_digit():
    with pytest.raises(ValueError):
        get_mask_account('736541084301358743bb')
