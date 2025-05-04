#Первое задание
skills = ["Python", "Git", "Docker", "Git", "Python", "FastAPI"]
print(set(skills))
#Второе задание
user1 = {"Python", "Docker", "Git"}
user2 = {"Python", "FastAPI", "Docker"}
print(user1 & user2)
print(user1 - user2)
print(user2 - user1)
#Третье задание
user = ("Gleb", 26, "Минск")
print(f"Имя: {user[0]}")
print(f"Возраст: {user[1]}")
print(f"Город: {user[2]}")
#Четвертое задание
cities = {
    ("Минск", "Беларусь"): 2000000,
    ("Берлин", "Германия"): 3700000
}
print(cities.get(("Минск", "Беларусь")))
cities["Варшава", "Польша"] = 1700000
print(cities)