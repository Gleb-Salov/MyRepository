class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0 or value > 150:
            raise ValueError("Incorrect: age must be > than 0 and < then 150")
        self._age = value