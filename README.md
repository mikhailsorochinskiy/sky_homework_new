# sky_homework_new

## Описание:
Проект по созданию виджета банковских операций клиента

## Установка:
Клонирование с удаленного репозитория:
```
git clone https://github.com/mikhailsorochinskiy/sky_homework_new.git
```
### Установка зависимостей:
Для пользователя:
```
poetry install --no--dev
```
Для разработчика:
```
poetry install
```

## Пример использования:
В командной строке выполните команду и вводите данные для функций
```
python main.py
```
В модуле generators.py или в main.py(сделать импорт из generators.py) запустить функции filter_by_currency
 и 
transaction_descriptions. Функции принимают список словарей. Вот пример:
```
transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)
```
## Тестирование функций:
В командной строке выполните команду
```
pytest
```
Проверка, сколько процентов кода было протестировано:
```
pytest --cov
```
Чтобы создать html-файл о процентах тестирования:
```
pytest --cov=src --cov-report=html
```