students = [
    {"name": "Аня", "scores": {"math": 5, "history": 4, "biology": 5}},
    {"name": "Борис", "scores": {"math": 2, "history": 3, "biology": 2}},
    {"name": "Вика", "scores": {"math": 4, "history": 5, "biology": 5}},
    {"name": "Глеб", "scores": {"math": 5, "history": 5, "biology": 5}},
]
print("\n" + "-" * 40 + "\n") 
# 🎯 Тебе нужно реализовать последовательно:

# ✅ Функцию get_average_scores(students)
# Возвращает словарь {имя: средний_балл} с округлением до 2 знаков после запятой.

def get_average_scores(students: dict) -> dict:
    result = {
        student["name"]: round(sum(student["scores"].values()) / len(student["scores"]), 2)
        for student in students
        }
    return result

average_scores = get_average_scores(students)
print(average_scores)
print("\n" + "-" * 40 + "\n") 
                            # ✅ Разделители между частями отчёта — print("-" * 40)
                            # ✅ Вызови все функции, выведи результат, 
                            # строго по смыслу отчёта.

# ✅ Функцию get_excellent_students(average_scores)
# Возвращает список имён учеников с средним баллом ≥ 4.5

def get_excellent_students(average_scores: dict) -> list:
    result = [
        student_name for student_name, score in average_scores.items()
        if score >= 4.5
        ]
    return result

excellent_students = get_excellent_students(average_scores)
print(excellent_students)
print("\n" + "-" * 40 + "\n") 

# ✅ Функцию get_failed_subjects(students)
# Возвращает словарь {имя: [названия_предметов_где_оценка<4]}
# (если у ученика всё хорошо — его в словаре нет)

def get_failed_subjects(students: dict) -> dict:
    result = {
         student["name"]: 
         [subject for subject, score in student["scores"].items() if score < 4] 
         for student in students
         if any(score < 4 for score in student["scores"].values())
         }
    return result

failed_subjects = get_failed_subjects(students)
print(failed_subjects)
print("\n" + "-" * 40 + "\n") 

# ✅ Генератор low_scores(students)
# Генерирует кортежи (имя, предмет, оценка) для всех оценок < 4

def low_scores(students):
    for student in students:
        for subject, score in student["scores"].items():
            if score < 4:
                yield(student["name"], subject, score)

for name, subject, score in low_scores(students):
    print(f"{name}: {subject} — {score}")
print("\n" + "-" * 40 + "\n") 
