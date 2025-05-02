# sum(iterable, start=0)
# min(iterable[, key=...])
# max(iterable[, key=...]

# Дано:
students = [
    {"name": "Аня", "math": 80},
    {"name": "Борис", "math": 55},
    {"name": "Вика", "math": 92},
    {"name": "Глеб", "math": 67}
]

# 1. Вычисли сумму всех оценок по математике

print(sum(student["math"] for student in students))

# 2. Найди студента с максимальной оценкой

print(max(students, key = lambda s: s["math"]))

# 3. Найди студента с минимальной оценкой

print(min(students, key = lambda s: s["math"]))