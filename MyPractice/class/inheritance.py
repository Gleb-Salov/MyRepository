class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def __str__(self) -> str:
        return f"Employee name = {self.name}, salary = {self.salary}"
    
class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department

    def __str__(self) -> str:
        return f"Manager name = {self.name}, salary = {self.salary}, department = {self.department}"

class Developer(Employee):
    def __init__(self, name: str, salary: float, language: str):
        super().__init__(name, salary)
        self.language = language

    def __str__(self) -> str:
        return f"Developer name = {self.name}, salary = {self.salary}, language = {self.language}"

def describe(employee: Employee) -> None:
    if isinstance(employee, Manager):
        print(f"{employee.name} is a manager of {employee.department}")
    elif isinstance(employee, Developer):
        print(f"{employee.name} is a developer using {employee.language}")
    else:
        print(f"{employee.name} is a regular employee")

e1 = Employee("Ivan", 30000)
e2 = Manager("Gleb", 50000, "IT")
e3 = Developer("Oleg", 40000, "Python")

describe(e1)
describe(e2)
describe(e3)