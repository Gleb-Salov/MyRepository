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

users = [
    {"name": "Глеб", "skills": ["Python", "FastAPI", "Git"]},
    {"name": "Анна", "skills": ["HTML", "CSS", "Git"]},
    {"name": "Иван", "skills": ["Python", "Docker", "Git"]},
]
def skills_count(users: list):
    skills_count = {}

    for user in users:
        for skill in user["skills"]:
            if skill in skills_count:
                skills_count[skill] += 1
            else:
                skills_count[skill] = 1

    for skill, count in skills_count.items():
        print(f"{skill}: {count}")

skills_count(users)





