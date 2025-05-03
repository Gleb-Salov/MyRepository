# (expr for var in iterable if condition)

# Дано:
purchases = [
    {"user": "Аня", "amount": 120},
    {"user": "Борис", "amount": 80},
    {"user": "Аня", "amount": 30},
    {"user": "Глеб", "amount": 150},
    {"user": "Аня", "amount": 50},
]
# 1. Вычисли общую сумму покупок Ани

print(sum(user["amount"] for user in purchases if user["user"] == "Аня"))