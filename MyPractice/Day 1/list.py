def display_skills(skills: list[str] ) -> None:
    for skill in skills:
        print(f"Умею: {skill.strip()}") 

skills = ["Python", "SQL", "Git"]

skills.append("C#")
display_skills(skills)

skills.remove("Python")
display_skills(skills)

def upgrade_skills(skills: list[str]) -> list[str]:
    if "FastAPI" not in skills:
        skills.append("FastAPI")
    if "Docker" not in skills:
        skills.append("Docker")
    skills.sort()
    return skills

print(upgrade_skills(skills))


