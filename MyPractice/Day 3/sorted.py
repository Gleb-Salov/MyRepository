# sorted(список, key=lambda x: (x[0], x[1]))

# 🔹 Отсортируй список так, чтобы:
# Сначала шли товары с высшим рейтингом, при равном рейтинге — дешевле первым

products = [
    {"title": "Молоко", "price": 2.5, "rating": 4.5},
    {"title": "Хлеб", "price": 1.0, "rating": 4.8},
    {"title": "Сыр", "price": 5.0, "rating": 4.8},
    {"title": "Йогурт", "price": 1.5, "rating": 4.2},
    {"title": "Масло", "price": 3.0, "rating": 4.5}
]

products_rank = sorted(
    products,
    key = lambda product: (-product["rating"], product["price"])
)

print(products_rank)

# 🔹 Условия сортировки: Вперёд идут те, у кого меньше возраст
# При равном возрасте — у кого выше зарплата
# При равных зарплате и возрасте — по имени по алфавиту

employees = [
    {"name": "Алиса", "age": 30, "salary": 70000},
    {"name": "Борис", "age": 25, "salary": 80000},
    {"name": "Виктор", "age": 30, "salary": 80000},
    {"name": "Глеб", "age": 25, "salary": 70000},
    {"name": "Дана", "age": 30, "salary": 70000}
]

employees_sorted = sorted(
    employees,
    key = lambda employeer: (employeer["age"], -employeer["salary"], employeer["name"])
)

print(employees_sorted)