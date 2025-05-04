# filter(функция_условия, коллекция)

# Отфильтруй студентов так, чтобы остались только те, у кого math >= 70.

students = [
    {"name": "Аня", "math": 80},
    {"name": "Борис", "math": 55},
    {"name": "Вика", "math": 92},
    {"name": "Глеб", "math": 67}
]

best_students = list(filter(lambda student: student["math"] >=70, students))
print(best_students)