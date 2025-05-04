# map(function, iterable)
# function: функция, принимающая 1 аргумент и возвращающая изменённое значение
# iterable: коллекция, по которой проходим

# Задание:
# Создай новый список, где будут только имена студентов в верхнем регистре (.upper())

students = [
    {"name": "Аня", "math": 80},
    {"name": "Борис", "math": 55},
    {"name": "Вика", "math": 92},
    {"name": "Глеб", "math": 67}
]

big_name_students = list(map(lambda student: student["name"].upper(), students))
print(big_name_students)