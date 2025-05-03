# Дано:
purchases = [
    {"category": "еда", "amount": 12.5},
    {"category": "транспорт", "amount": 5.0},
    {"category": "еда", "amount": 7.5},
    {"category": "развлечения", "amount": 15.0},
    {"category": "транспорт", "amount": 10.0},
    {"category": "еда", "amount": 6.0}
]
# 1. Используя defaultdict(float), посчитай сумму трат по каждой категории.
# Выведи итог в виде обычного словаря:{'еда': 26.0, 'транспорт': 15.0, 'развлечения': 15.0}

from collections import defaultdict
category_sum = defaultdict(float)

for purchas in purchases:
    category_sum[purchas["category"]] += purchas["amount"]     

print(dict(category_sum))

# 2. Посчитай, сколько покупок приходится на каждую категорию.
# Ожидаемый вывод:{'еда': 3, 'транспорт': 2, 'развлечения': 1}

category_count = defaultdict(int)

for purchas in purchases:
    category_count[purchas["category"]] += 1

print(dict(category_count))