def check_temperature(temperature: int | float | str) -> str:
    try:
        temperature = float(temperature)
    except ValueError:
        return "Ошибка: температура должна быть числом"
    if temperature < 0:
        return "Очень холодно!"
    elif 0 <= temperature < 15:
        return "Прохладно."
    elif 15 <= temperature < 25:
        return "Комфортно"
    else:
        return "Жарко!"
print(check_temperature(15))
print(check_temperature("abc"))  # Ошибка: температура должна быть числом     
        