print("\n" + "-" * 40 + "\n") 
# Дано:
names = ["Аня", "Борис", "Вика", "Глеб"]
math = [80, 55, 92, 67]
eng  = [72, 60, 88, 75]

# Задания:
# 1. Объедини names, math, eng в список студентов с полями:

student_diarys = [
    {"name":name, "math": math, "eng": eng}
    for name, math, eng in zip(names, math, eng)
]
print(student_diarys)
print("\n" + "-" * 40 + "\n") 

# 2. Отфильтруй тех, у кого и математика, и английский ≥ 70

good_students = list(
    filter(
        lambda s: s["math"] >= 70 and s["eng"] >= 70,
        student_diarys
    )
)

print(good_students)
print("\n" + "-" * 40 + "\n") 

# 3. Преобразуй результат: оставь только ИМЕНА (в верхнем регистре)

big_names = list(map(lambda s: s["name"].upper(), good_students))
print(big_names)
print("\n" + "-" * 40 + "\n")

# 4. Все ли студенты сдали оба предмета на ≥ 70;
# хотя бы один студент имеет math > 90

if all(student["math"] >=70 and student["eng"] >=70 for student in good_students):
    print("Все студенты сдали оба предмета на ≥ 70")

if any(student["math"] >90 for student in good_students):
    print(f"{[s['name'] for s in good_students if s['math'] > 90]} имеет math > 90")
print("\n" + "-" * 40 + "\n")
