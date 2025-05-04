# Дано
purchases = [
    {"user": "Аня", "month": "Январь", "amount": 100.0},
    {"user": "Борис", "month": "Январь", "amount": 50.0},
    {"user": "Аня", "month": "Январь", "amount": 50.0},
    {"user": "Аня", "month": "Февраль", "amount": 100.0},
    {"user": "Глеб", "month": "Февраль", "amount": 200.0},
]
from collections import defaultdict
# 1. Сгруппировать траты по месяцу, а внутри — по пользователю, посчитав итоговую сумму.

result = defaultdict(lambda: defaultdict(float))

for purchase in purchases:
    user = purchase["user"]
    month = purchase["month"]
    amount = purchase["amount"]
    result[month][user] += amount

clear_result = {
    month: dict(user)
    for month, user in result.items()
}

import pprint
pprint.pprint(dict(clear_result))