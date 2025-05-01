def upgrade_profile(user: dict) -> dict:
    if "skills" in user:
        if "Docker" not in user["skills"]:
            user["skills"].append("Docker")
        if "Linux" not in user["skills"]:
            user["skills"].append("Linux")
        user["skills"].sort()
    else:   
        user["skills"] = ["Docker", "Linux"]    
    return user
# Пример использования функции  
profile = {
    "name": "Глеб",
    "age": 26,
    "skills": ["Python", "FastAPI"]
}
upgrade_profile(profile)
print(profile)  # {'name': 'Глеб', 'age': 26, 'skills': ['Docker', 'FastAPI', 'Linux', 'Python']}