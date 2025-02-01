# sky_homework_new

## Описание:
Проект по созданию виджета банковских операций клиента. В папке src лежат модули функций.
Программа начинает работу из модуля main.py, который находится в корне проекта

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
В командной строке выполните команду и выберите тип файла, а также варианты фильтрации.
```
python main.py
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
## Данные для работы с проектом:
В директории ./data находятся файлы с разным форматом данных: json, csv, excel.
Чтобы использовать данные из json-файла, нужно воспользоваться модулем utils.py из пакета src.
А для файлов с форматом csv или excel модулем csv_excel.py