# Дано:
users = ["Аня", "Борис", "Вика"]
categories = ["еда", "техника", "развлечения"]
amounts = [250, 990, 500]

# Объедини списки с помощью zip и выведи такие строки:

# Аня купила еда на 250
# Борис купил техника на 990
# Вика купила развлечения на 500

for user, category, amount in zip(users, categories, amounts):
    if user in ("Аня", "Вика"):
        print(f"{user} купила {category} на {amount}")
    else:
        print(f"{user} купил {category} на {amount}")