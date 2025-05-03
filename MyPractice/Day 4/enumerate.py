# enumerate(iterable, start=0)
# Принимает итерируемый объект (список, строку, генератор и т.д.)
# Возвращает итератор кортежей вида (индекс, значение)

# Дано:
purchases = [
    {"user": "Аня", "amount": 200},
    {"user": "Борис", "amount": 150},
    {"user": "Аня", "amount": 300},
    {"user": "Аня", "amount": 100},
    {"user": "Борис", "amount": 50},
    {"user": "Аня", "amount": 500},
]
from collections import defaultdict
# 1. Написать генератор every_second_purchase(purchases),
# который будет по одному возвращать каждую вторую покупку (по порядку)
# для каждого пользователя.

def every_second_purchase(purchases):
    users = defaultdict(list)

    for item in purchases:
        name = item["user"]
        users[name].append(item)  # users {аня: [{},{},...], борис:[{},{},...]}

    for name, value in users.items():
        for index, purchas in enumerate(value):
            if index % 2 == 1:
                yield purchas

for purchas in every_second_purchase(purchases):
    print(purchas)
