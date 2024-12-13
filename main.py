from src.widget import mask_account_card, get_date

card_number = input("Введите номер карты или счета: ")
operation_date = input("Введите дату: ")

if __name__ == "__main__":
    print(mask_account_card(card_number))
    print(get_date(operation_date))
