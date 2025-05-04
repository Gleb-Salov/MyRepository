# Дано:
from collections import defaultdict
purchases = [
    {"user": "Алиса", "category": "еда", "amount": 25.5},
    {"user": "Борис", "category": "транспорт", "amount": 15.0},
    {"user": "Алиса", "category": "еда", "amount": 14.5},
    {"user": "Алиса", "category": "развлечения", "amount": 40.0},
    {"user": "Борис", "category": "еда", "amount": 20.0},
]
# Сгруппировать данные по пользователю и категории,
# чтобы получить итоговую сумму потраченного по каждой категории для каждого пользователя

result = defaultdict(lambda: defaultdict(float))

for purches in purchases:
    user = purches["user"]
    category = purches["category"]
    amount = purches["amount"]

    result[user][category] += amount

pretty_result = {
    name: dict(categories)
    for name, categories in result.items()
}

import pprint
pprint.pprint(dict(pretty_result))