def get_contact(user: dict, method: str) -> str:
    return user.get("contacts", {}).get(method, "Контакт не найден")

user = {
    "name": "Глеб",
    "age": 26,
    "skills": ["Python", "FastAPI"],
    "contacts": {
        "email": "gleb@example.com",
        "telegram": "@glebdev"
    }
}

print(get_contact(user, "email"))