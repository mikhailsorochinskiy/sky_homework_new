import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
        (28014, 28016, ["0000 0000 0002 8014", "0000 0000 0002 8015", "0000 0000 0002 8016"]),
    ],
)
def test_card_number_generator(start, end, expected):
    card_number = card_number_generator(start, end)
    for result in expected:
        assert next(card_number) == result


def test_card_number_generator_start_lower_stop():
    card_number = card_number_generator(3, 2)
    assert print(*card_number) is None


def test_card_number_generator_start_or_stop_bigger16():
    card_number = card_number_generator(10000000000000000, 10000000000000001)
    assert print(*card_number) is None
