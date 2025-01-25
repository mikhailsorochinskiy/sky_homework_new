import pandas as pd


def get_transactions_from_csv(filename: str) -> list[dict]:
    """ Функция принимает csv-файл с транзакциями и возвращает список словарей"""
    df = pd.read_csv(f'../data/{filename}', delimiter=';')
    return df.to_dict(orient='records')


def get_transactions_from_excel(filename: str) -> list[dict]:
    """ Функция принимает excel-файл с транзакциями и возвращает список словарей"""
    df = pd.read_excel(f'../data/{filename}')
    return df.to_dict(orient='records')
