from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

card_number = input("Введите номер карты или счета: ")
operation_date = input("Введите дату: ")
state = input("Введите значение по умолчанию")
sort_option = bool(input("Введите True, если по убыванию, False - по возрастанию"))
id_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

if __name__ == "__main__":
    print(mask_account_card(card_number))
    print(get_date(operation_date))
    print(filter_by_state(id_list, "EXECUTED"))
    print(sort_by_date(id_list, sort_option=True))
