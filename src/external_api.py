import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_amount_transaction(transaction: dict) -> float:
    """Функция принимает транзакцию и возвращает ее сумму"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    currency_from = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_from}&amount={amount}"
    payload = {}
    headers = {"apikey": API_KEY}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()["result"]
