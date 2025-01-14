from src.decorators import log
from src.masks import get_mask_account, get_mask_card_number


def test_divide():
    @log(filename="")
    def divide(a, b):
        return a / b

    result = divide(3, 0)
    assert result == "divide error: ZeroDivisionError. Inputs: (3, 0), {}"


def test_add():
    @log(filename="mylog.txt")
    def add_args(a, b):
        return a + b

    result = add_args(1, 2)
    assert result == "add_args 3"


def test_get_mask_card_number_with_decorator():
    decorated_function = log(filename="")(get_mask_card_number)
    result = decorated_function("1234567887654321")
    assert result == "get_mask_card_number 1234 56** **** 4321"


def test_get_mask_account_with_decorator():
    decorated_function = log(filename="")(get_mask_account)
    result = decorated_function("1234567887654321")
    assert result == "get_mask_account error: ValueError. Inputs: ('1234567887654321',), {}"
