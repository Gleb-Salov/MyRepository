# Дано:
users = [
    {"name": "Аня", "purchases": {"еда": [120, 230], "развлечения": [300]}},
    {"name": "Борис", "purchases": {"еда": [100], "транспорт": [50, 70]}},
    {"name": "Вика", "purchases": {"развлечения": [150, 100], "транспорт": [80]}},
]
# 1. Создай словарь total_spent, где:
# ключ — имя пользователя
# значение — сумма всех его трат

total_spent = {
    user["name"]: sum(sum(costs) for costs in user["purchases"].values())
    for user in users
}

print(total_spent)

# 2.  Создай словарь category_stats, где:
# ключ — название категории (напр. "еда")
# значение — общая сумма по всем пользователям в этой категории

from collections import defaultdict

category_stats = defaultdict(int)

for user in users:
    for category, costs in user["purchases"].items():
        category_stats[category] += sum(costs)

print(dict(category_stats))

# 3. Найди всех, кто потратил больше 300, и выведи их имена.

for user, value in total_spent.items():
    if value >= 300:
        print(user)

# 4. Найти пользователя с максимальными тратами?

max_spender = max(total_spent, key=lambda name: total_spent[name])
print(max_spender)


     