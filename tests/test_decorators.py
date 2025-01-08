from src.decorators import log
from src.masks import get_mask_card_number, get_mask_account


def test_divide():
    @log(filename='')
    def divide(a, b):
        return a / b

    result = divide(3, 0)
    assert result == 'divide error: ZeroDivisionError. Inputs: (3, 0), {}'


def test_add():
    @log(filename='mylog.txt')
    def add_args(a, b):
        return a + b

    result = add_args(1, 2)
    assert result == 'add_args 3'

# def sss():
#     return get_mask_card_number

def test_get_mask_card_number_with_decorator():
    @log(filename='')
    # @wraps(get_mask_card_number)
    def get_mask_card_number_with_decorator():
        return get_mask_card_number('1234567887654321')

    assert get_mask_card_number_with_decorator() == 'get_mask_card_number_with_decorator 1234 56** **** 4321'


def test_get_mask_account_with_decorator():
    @log(filename='')
    def get_mask_account_with_decorator():
       return get_mask_account('1234567887654321')
    assert get_mask_account_with_decorator() == ('get_mask_account_with_decorator error: ValueError. Inputs: '
                                                 '(), {}')
