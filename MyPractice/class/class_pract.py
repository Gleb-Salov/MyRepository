class Rectangle:
    # конструктор класса в Python
    def __init__(self, width: int = 0, height: int = 0) -> None:
        if width < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative")
        self.width = width
        self.height = height
   
    def area(self) -> int:
        area = self.width * self.height
        return area
    
    def perimeter(self) -> int:
        perimeter = 2*(self.width + self.height)
        return perimeter
    
    def __str__(self) -> str: # отвечает за вывод print(odj)
        return f"{self.width}×{self.height} прямоугольник"
    
    def __repr__(self) -> str: # инструмент разработчика для отладки
        return f"Rectangle(width={self.width}, height={self.height})"

r = Rectangle(2, 4)
print(r)
print(repr(r))
print(r.area())      # 12
print(r.perimeter()) # 14