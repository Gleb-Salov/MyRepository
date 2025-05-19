class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.age == other.age
        
p1 = Person("Глеб", 25)
p2 = Person("Глеб", 25)
p3 = Person("Олег", 30)

print(p1 == p2)  # True — имя и возраст совпадают
print(p1 == p3)  # False — разные данные
print(p1 == "просто строка")  # False, но без ошибки
