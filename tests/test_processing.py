import pytest

from src.processing import filter_by_state, sort_by_date

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

data_no_state = [
    {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
]


@pytest.fixture()
def get_data():
    return data


@pytest.mark.parametrize('state, expected', [('EXECUTED', [{"id": 41428829,
                                                            "state": "EXECUTED",
                                                            "date": "2019-07-03T18:35:29.512364"},
                                                           {"id": 939719570,
                                                            "state": "EXECUTED",
                                                            "date": "2018-06-30T02:08:58.425572"}]),
                                             ('CANCELED', [{"id": 594226727,
                                                            "state": "CANCELED",
                                                            "date": "2018-09-12T21:27:25.241689"},
                                                           {"id": 615064591,
                                                            "state": "CANCELED",
                                                            "date": "2018-10-14T08:21:33.419441"}])
                                             ])
def test_filter_by_state(get_data, state, expected):
    assert filter_by_state(get_data, state) == expected


@pytest.fixture()
def result_data():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]


def test_filter_by_state_no_user_state(get_data, result_data):
    assert filter_by_state(get_data) == result_data


@pytest.fixture()
def get_data_no_state():
    return data_no_state


def test_filter_by_state_no_state(get_data_no_state):
    with pytest.raises(ValueError):
        filter_by_state(get_data_no_state, state='EXECUTED')


@pytest.mark.parametrize('sort_option, expected',
                         [(True, [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                  {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                                  {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                  {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]),
                          (False, [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                   {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                   {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                                   {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]), ])
def test_sort_by_date(get_data, sort_option, expected):
    assert sort_by_date(get_data, sort_option) == expected


@pytest.fixture()
def result_data_no_sort():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]


def test_sort_by_date_with_no_sort(get_data, result_data_no_sort):
    assert sort_by_date(get_data) == result_data_no_sort


@pytest.fixture()
def data_with_same_data():
    return [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 594226722, "state": "CANCELED", "date": "2018-09-12T22:27:25.241689"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 41428822, "state": "EXECUTED", "date": "2019-07-03T19:35:29.512364"}]


def test_sort_by_date_with_same_data(data_with_same_data):
    assert sort_by_date(data_with_same_data, True) == [
        {"id": 41428822, "state": "EXECUTED", "date": "2019-07-03T19:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226722, "state": "CANCELED", "date": "2018-09-12T22:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]


def test_sort_by_date_invalid_data():
    with pytest.raises(ValueError):
        sort_by_date([{"id": 594226727, "state": "CANCELED", "date": "201809-12T21:27:25.241689"},
                      {"id": 594226722, "state": "CANCELED", "date": "2018-09-12R22:27:25.241689"}])
