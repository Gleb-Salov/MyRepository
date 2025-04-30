while True:
    password = input("Введите пароль: ")
    if password == "admin123":
        print("Доступ разрешён")
        break
    else:
        print("Неверный пароль")