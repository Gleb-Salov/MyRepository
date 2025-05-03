# Дано:
purchases = [
    {"user": "Аня", "category": "еда", "amount": 120},
    {"user": "Глеб", "category": "транспорт", "amount": 300},
    {"user": "Аня", "category": "транспорт", "amount": 100},
    {"user": "Глеб", "category": "еда", "amount": 220},
    {"user": "Аня", "category": "одежда", "amount": 500},
]
# 1. Напиши функцию-генератор get_user_purchases(purchases, name),
# которая будет по одному возвращать покупки указанного пользователя name.

def get_user_purchases(purchases, name: str):
    for user in purchases:
        if user["user"] == name:
            yield user 

for user in get_user_purchases(purchases, "Аня"):
    print(user)
    
print("\n" + "-" * 40 + "\n") 
# 2. Напиши функцию-генератор filter_by_category(purchases, category),
# которая будет по одной возвращать только те покупки,
# у которых поле "category" совпадает с переданным аргументом category.

def filter_by_category(purchases, category):
    for user in purchases:
        if user["category"] == category:
            yield user 

for user in filter_by_category(purchases, "еда"):
    print(user)