def multiply_table(n):
    try:
        n = float(n)  # пробуем преобразовать в число с плавающей точкой
    except ValueError:
        print("Ошибка: переменная не является числом")
        return

    for i in range(1, 11):
        print(f"{i} * {n} = {i * n}")
