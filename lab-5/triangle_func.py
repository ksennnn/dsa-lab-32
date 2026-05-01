class IncorrectTriangleSides(Exception):
    # Исключение, возникающее при некорректных сторонах треугольника
    pass


def get_triangle_type(side1, side2, side3):
    # Проверка на отрицательные или нулевые стороны
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise IncorrectTriangleSides("Стороны треугольника должны быть положительными числами")
    
    # Проверка неравенства треугольника
    if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
        raise IncorrectTriangleSides("Стороны не удовлетворяют неравенству треугольника")
    
    # Определение типа треугольника
    if side1 == side2 == side3:
        return "equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "isosceles"
    else:
        return "nonequilateral"