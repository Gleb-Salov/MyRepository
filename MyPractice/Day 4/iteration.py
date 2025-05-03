# Дано:
students = ["Аня", "Борис", "Вика"]

it = iter(students)
try:    
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print("конец списка")

# Дано:
purchases = [
    {"user": "Аня", "category": "еда", "amount": 120, "month": "январь"},
    {"user": "Аня", "category": "одежда", "amount": 300, "month": "январь"},
    {"user": "Борис", "category": "еда", "amount": 150, "month": "февраль"},
    {"user": "Аня", "category": "еда", "amount": 210, "month": "февраль"},
    {"user": "Глеб", "category": "развлечения", "amount": 500, "month": "март"},
    {"user": "Борис", "category": "техника", "amount": 250, "month": "март"},
    {"user": "Глеб", "category": "еда", "amount": 100, "month": "апрель"},
]
from collections import defaultdict
# 1. Напиши функцию-генератор category_avg(purchases),
# которая по одному будет возвращать пары: категория → средний чек по этой категории.

def category_avg(purchases):
    
    total = defaultdict(float)
    count = defaultdict(int)

    for item in purchases:
        category = item["category"]
        total[category] += item["amount"]
        count[category] += 1
    for category in total:    
        yield (category, total[category]/count[category])

for category, avg in category_avg(purchases):
    print(f"{category}: средний чек — {avg:.2f}")