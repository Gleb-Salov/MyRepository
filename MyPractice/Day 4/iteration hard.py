# Дано:
purchases = [
    {"user": "Аня", "category": "еда", "amount": 250},
    {"user": "Аня", "category": "техника", "amount": 990},
    {"user": "Борис", "category": "еда", "amount": 300},
    {"user": "Аня", "category": "еда", "amount": 180},
    {"user": "Борис", "category": "еда", "amount": 220},
    {"user": "Борис", "category": "техника", "amount": 1200},
]
from collections import defaultdict
# 1. Напиши функцию-генератор user_category_avg(purchases),
# которая для каждого пользователя и категории будет возвращать средний чек.

def user_category_avg(purchases):
    count = defaultdict(int)
    total = defaultdict(float)

    for item in purchases:
        name = item["user"]
        category = item["category"]
        count[(name, category)]+= 1
        total[(name, category)]+= item["amount"] 

    for name, category in total:  
        yield (name, category, (total[(name, category)]/count[(name, category)]))

for name, category, avg in user_category_avg(purchases):
    print(f"{name} в категории {category} потратил(ла):{avg:.2f} деняк")