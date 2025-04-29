def analyze_person_info(info: dict) -> str:
    try:
        # Преобразуем возраст и сохраняем его в словарь
        age = int(info.get("age"))
        info["age"] = f"{age} лет"
        
        # Преобразуем температуру и добавляем описание
        temperature = int(info.get("temperature"))
        if temperature < 0:
            info["temperature"] = f"{temperature}°C - Очень холодно!"
        elif 0 <= temperature < 15:
            info["temperature"] = f"{temperature}°C - Прохладно."
        elif 15 <= temperature < 25:
            info["temperature"] = f"{temperature}°C - Комфортно"
        else:
            info["temperature"] = f"{temperature}°C - Жарко!"
    except (ValueError, TypeError):
        return "Ошибка: возраст и температура должны быть числами"

    # Формируем строку из всех значений словаря
    result = ""
    for value in info.values():
        result += str(value) + ", "

    return result.rstrip(", ")

# Пример
info = {
    "name": "Иван",
    "age": "30",
    "city": "Москва",
    "temperature": "22"
}
print(analyze_person_info(info))
