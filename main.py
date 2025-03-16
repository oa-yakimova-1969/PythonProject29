from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

info = input("Введите номер карты или счета:")
date_str = input("Введите дату:")

transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(mask_account_card(info))
print(get_date(date_str))
print(filter_by_state(transactions, state="EXECUTED"))
print(sort_by_date(transactions, reverse=True))
