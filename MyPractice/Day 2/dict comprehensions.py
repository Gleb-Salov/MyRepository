users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30},
    {"name": "Diana", "age": 15},
    {"name": "Eve", "age": 22}
]

# Задание: сгенерируй список имён только тех пользователей, которым 18 лет и больше.

print("\n" + "-" * 40 + "\n")  
adult = [user["name"] for user in users if user["age"] >= 18]
print(adult)
print("\n" + "-" * 40 + "\n")  

adult_users = {user["name"]: "совершеннолетний" if user["age"] >= 18 else "несовершеннолетний" for user in users}
print(adult_users)
print("\n" + "-" * 40 + "\n")  

# Задание: С помощью вложенного генератора создать один список
# только с баллами выше 80 (включительно) — и вывести его.

scores = [
    [75, 88, 92],
    [60, 70],
    [95, 100, 85],
    [50]
]

top_scores = [mark for score in scores for mark in score if mark >= 80]
print(top_scores)
print("\n" + "-" * 40 + "\n")  

# Задание: cоздай словарь вида:{"Alice": 85, "Bob": 92, "Charlie": 60} 
# где ключи — имена, а значения — оценка по математике.

students = [
    {"name": "Аня", "scores": {"math": 5, "history": 2}},
    {"name": "Борис", "scores": {"math": 3, "history": 4}},
    {"name": "Вика", "scores": {"math": 5, "history": 5}},
]

students_score = {
    student["name"]: student["scores"]["math"]
    for student in students
}
print(students_score)
print("\n" + "-" * 40 + "\n")  

# Задание: cоздай словарь, 
# в котором ключ — это имя ученика, а значение — средний балл по всем предметам.

students_average = {
    student["name"]: sum(student["scores"].values()) / len(student["scores"])
    for student in students
}
print(students_average)
print("\n" + "-" * 40 + "\n") 

# Задача: создай словарь вида {имя: [все оценки выше 3]}

good_scores = {
    student["name"]:
    [score for score in student["scores"].values() if score >=3]
    for student in students
}
print(good_scores)
print("\n" + "-" * 40 + "\n") 

# Задача: {имя: [предметы с оценкой выше 3]}

good_subjects = {
    student["name"]: [subject for subject, score in student["scores"].items() if score > 3]
    for student in students
}
print(good_subjects)