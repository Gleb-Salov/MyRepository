def parse_skills(skills:str) -> list:
    result = [skill.strip() for skill in skills.split(",")]
    return result
#Example usage:
ex = "Python, FastAPI, SQL , Git "
print(parse_skills(ex)) # ['Python', 'FastAPI', 'SQL', 'Git']
