# users = [
#     {"name": "Глеб", "skills": ["Python", "FastAPI"]},
#     {"name": "Анна", "skills": ["HTML", "CSS", "JS"]},
# ]
# for user in users:
#     print(f'{user["name"]} умеет:')
#     for i, skill in enumerate(user["skills"], start=1):
#         print(f"{i}. {skill}")

# tasks = ["написать код", "сделать коммит", "запушить в GitHub"]
# for i, task in enumerate(tasks, start=1):
#     print(f'{i}.{task}') 

# users = [
#     {"name": "Глеб", "skills": ["Python", "FastAPI", "Git"]},
#     {"name": "Анна", "skills": ["HTML", "CSS", "Git"]},
#     {"name": "Иван", "skills": ["Python", "Docker", "Git"]},
# ]
# def skills_count(users: list):
#     skills_count = {}

#     for user in users:
#         for skill in user["skills"]:
#             if skill in skills_count:
#                 skills_count[skill] += 1
#             else:
#                 skills_count[skill] = 1

#     for skill, count in skills_count.items():
#         print(f"{skill}: {count}")

# skills_count(users)

# from collections import Counter
# skills = ["Python", "Docker", "Git", "Docker", "FastAPI", "Python", "Python"]
# counter = Counter(skills)
# for skill, count in counter.items():
#     print(f"{skill}: {count}")

from collections import Counter
users_skills = [
    ["Python", "Docker", "Git"],
    ["Python", "FastAPI", "Docker"],
    ["Python", "Docker"],
    ["Git", "FastAPI"],
    ["Python"]
]
all_skills = []
for skill in users_skills:
    all_skills += skill #Или all_skills.extend(skill)
print(Counter(all_skills))

top3 = Counter(all_skills).most_common(3)
print(top3)

