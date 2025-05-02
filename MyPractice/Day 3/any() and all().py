# any()	True, если хотя бы один элемент True
# all()	True, если все элементы True
# возвращают bool

# Задание: проверь два условия: 1) Все ли оценки не ниже 60
# 2) Есть ли хоть одна оценка выше 85

grades = [80, 65, 90, 72]

print(all(grade >= 60 for grade in grades)) # True
print(any(grade > 85 for grade in grades)) # True