import sys

from src.csv_excel import get_transactions_from_csv, get_transactions_from_excel
from src.filtered import get_list_with_main_string
from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.utils import get_operations_from_json
from src.widget import get_date, mask_account_card


def main():
    type_file = input("Программа: Привет! Добро пожаловать в программу работы\n"
                      "с банковскими транзакциями. Выберите необходимый пункт меню:\n"
                      "1. Получить информацию о транзакциях из JSON-файла\n"
                      "2. Получить информацию о транзакциях из CSV-файла\n"
                      "3. Получить информацию о транзакциях из XLSX-файла\n")
    if not type_file.isdigit():
        print("Введено неправильное значение")
        sys.exit()
    if int(type_file) == 1:
        print("Программа: Для обработки выбран JSON-файл.")
        data = get_operations_from_json('data/operations.json')
    elif int(type_file) == 2:
        print("Программа: Для обработки выбран CSV-файл.")
        data = get_transactions_from_csv('transactions.csv')
    elif int(type_file) == 3:
        print("Программа: Для обработки выбран XLSX-файл.")
        data = get_transactions_from_excel('transactions_excel.xlsx')
    else:
        print("Введено неправильное значение")
        sys.exit()
    while True:
        operations_status = input("Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
                                  "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").upper()
        if operations_status == 'EXECUTED' or operations_status == 'CANCELED' or operations_status == 'PENDING':
            data = filter_by_state(data, operations_status)
            break
        else:
            print(f'Программа: Статус операции {operations_status} недоступен.')

    is_sort = input("Программа: Отсортировать операции по дате? Да/Нет ").upper()
    if is_sort == 'ДА':
        sort_option = input("Программа: Отсортировать по возрастанию или по убыванию? ").upper()
        if sort_option == 'ПО ВОЗРАСТАНИЮ':
            data = sort_by_date(data, False)
        else:
            data = sort_by_date(data)

    is_only_rub_operations = input("Программа: Выводить только рублевые транзакции? Да/Нет ").upper()
    if is_only_rub_operations == 'ДА':
        data = list(filter_by_currency(data, 'RUB'))

    is_sort_main_word = input("Программа: Отфильтровать список транзакций по определенному слову в описании? "
                              "Да/Нет ").upper()
    if is_sort_main_word == 'ДА':
        search_text = input("Введите ключевое слово(слова))\n")
        data = get_list_with_main_string(data, search_text)
    descriptions = transaction_descriptions(data)
    if len(data) == 0:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    else:
        print(f'Программа: Распечатываю итоговый список транзакций...'
              f'Программа: '
              f'Всего банковских операций в выборке: {len(data)}')
        for transaction in data:
            print(f'{get_date(transaction.get('date'))} {next(descriptions)}')
            if transaction.get('description') == 'Открытие вклада':
                if int(type_file) == 1:
                    print(f'{mask_account_card(transaction.get('to'))}\n'
                          f'Сумма: {transaction.get('operationAmount').get('amount')} '
                          f'{transaction.get('operationAmount').get('currency').get('code')}')
                else:
                    print(f'{mask_account_card(transaction.get('to'))}\n'
                          f'Сумма: {transaction.get('amount')} {transaction.get('currency_code')}')
            else:
                if int(type_file) == 1:
                    print(f'{mask_account_card(transaction.get('from'))} -> '
                          f'{mask_account_card(transaction.get('to'))}\n'
                          f'Сумма: {transaction.get('operationAmount').get('amount')} '
                          f'{transaction.get('operationAmount').get('currency').get('code')}')
                else:
                    print(f'{mask_account_card(transaction.get('from'))} -> '
                          f'{mask_account_card(transaction.get('to'))}\n'
                          f'Сумма: {transaction.get('amount')} {transaction.get('currency_code')}')


if __name__ == "__main__":
    main()
