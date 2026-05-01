class IncorrectTriangleSides(Exception):
    # Исключение, возникающее при некорректных сторонах треугольника
    pass


class Triangle:
    # Класс, описывающий треугольник.
    
    def __init__(self, side1, side2, side3):
        # Конструктор класса Triangle
        # Проверка на отрицательные или нулевые стороны
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise IncorrectTriangleSides("Стороны треугольника должны быть положительными числами")
        
        # Проверка неравенства треугольника
        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
            raise IncorrectTriangleSides("Стороны не удовлетворяют неравенству треугольника")
        
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def triangle_type(self):
        # Определяет тип треугольника
        if self.side1 == self.side2 == self.side3:
            return "equilateral"
        elif self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3:
            return "isosceles"
        else:
            return "nonequilateral"
    
    def perimeter(self):
        # Вычисляет периметр треугольника
        return self.side1 + self.side2 + self.side3