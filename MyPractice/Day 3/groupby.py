# Дано:
students = [
    {"name": "Аня", "group": "A"},
    {"name": "Борис", "group": "B"},
    {"name": "Вика", "group": "A"},
    {"name": "Глеб", "group": "B"},
    {"name": "Дана", "group": "A"}
]

# 1. Сгруппируй студентов по значению group, чтобы получился словарь:

result = {}
for student in students:
    group = student["group"]
    if group not in result:
        result[group] = []
    if student["name"][0] in 'АЕИОУЭЮЯГ':
        result[group].append(student["name"])
print(result)

# 2. Сгруппировать студентов по полю group
# Для каждой группы — посчитать среднюю оценку по математике

students2 = [
    {"name": "Аня", "group": "A", "math": 80},
    {"name": "Борис", "group": "B", "math": 90},
    {"name": "Вика", "group": "A", "math": 75},
    {"name": "Глеб", "group": "B", "math": 85},
    {"name": "Дана", "group": "A", "math": 81}
]

result2 = {}
for student in students2:
    group = student["group"]
    if group not in result2:
        result2[group] = []
    result2[group].append(student)

for group, members in result2.items():
    avg_math = sum(s["math"] for s in members) / len(members)
    print(f"Группа {group}: средняя оценка по математике — {avg_math:.2f}")

