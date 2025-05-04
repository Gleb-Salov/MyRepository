def process_user_input(data: dict) -> dict:
    # Создаем копию, чтобы не портить оригинальный словарь
    result = {}

    # 1. Имя, город — обрезаем пробелы
    result["name"] = data.get("name", "").strip()
    result["city"] = data.get("city", "").strip()

    # 2. Возраст
    try:
        result["age"] = int(data.get("age"))
    except (ValueError, TypeError):
        return "Ошибка: возраст должен быть числом"

    # 3. Email проверка
    email = data.get("email", "").strip()
    if "@" not in email:
        return "Ошибка: неверный формат электронной почты"
    result["email"] = email

    # 4. Skills (список строк) — разбиваем по запятой и убираем пробелы
    new_skills = data.get("skills", "")
    result["skills"] = [skill.strip() for skill in new_skills.split(",")]
    # 5. Подписка — yes/no → bool
    subscribe = data.get("subscribe", "").lower()
    if subscribe == "yes":
        result["subscribe"] = True
    elif subscribe == "no":
        result["subscribe"] = False
    else:
        return "Ошибка: неверный формат подписки"

    return result


# Тест
raw_data = {
    "name": "Анна",
    "age": "27",
    "email": "anna@example.com",
    "city": "Минск",
    "skills": "C#, ASP.NET, Git ",
    "subscribe": "yes"
}

print(process_user_input(raw_data))
        
