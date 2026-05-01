import pytest
from triangle_class import Triangle, IncorrectTriangleSides


# Позитивные тесты для создания объекта
def test_create_equilateral_triangle():
    # Тест создания равностороннего треугольника
    triangle = Triangle(3, 3, 3)
    assert triangle.side1 == 3
    assert triangle.side2 == 3
    assert triangle.side3 == 3


def test_create_isosceles_triangle():
    # Тест создания равнобедренного треугольника
    triangle = Triangle(5, 5, 8)
    assert triangle.side1 == 5
    assert triangle.side2 == 5
    assert triangle.side3 == 8


def test_create_nonequilateral_triangle():
    # Тест создания разностороннего треугольника
    triangle = Triangle(3, 4, 5)
    assert triangle.side1 == 3
    assert triangle.side2 == 4
    assert triangle.side3 == 5


def test_create_triangle_with_floats():
    # Тест создания треугольника с числами с плавающей точкой
    triangle = Triangle(2.5, 3.5, 4.5)
    assert triangle.side1 == 2.5
    assert triangle.side2 == 3.5
    assert triangle.side3 == 4.5


# Негативные тесты для создания объекта
def test_create_triangle_with_zero_side():
    # Тест создания треугольника с нулевой стороной
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 4, 5)


def test_create_triangle_with_negative_side():
    # Тест создания треугольника с отрицательной стороной
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-3, 4, 5)


def test_create_triangle_inequality_violation():
    # Тест создания треугольника с нарушением неравенства
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 3)


def test_create_triangle_degenerate():
    # Тест создания вырожденного треугольника
    with pytest.raises(IncorrectTriangleSides):
        Triangle(2, 3, 5)


# Позитивные тесты для метода triangle_type
def test_triangle_type_equilateral():
    # Тест определения равностороннего треугольника
    triangle = Triangle(4, 4, 4)
    assert triangle.triangle_type() == "equilateral"


def test_triangle_type_isosceles():
    # Тест определения равнобедренного треугольника
    triangle = Triangle(7, 7, 10)
    assert triangle.triangle_type() == "isosceles"


def test_triangle_type_isosceles_other():
    # Тест определения равнобедренного треугольника (другая комбинация)
    triangle = Triangle(8, 5, 5)
    assert triangle.triangle_type() == "isosceles"


def test_triangle_type_nonequilateral():
    # Тест определения разностороннего треугольника
    triangle = Triangle(6, 8, 10)
    assert triangle.triangle_type() == "nonequilateral"


# Позитивные тесты для метода perimeter
def test_perimeter_equilateral():
    # Тест периметра равностороннего треугольника
    triangle = Triangle(5, 5, 5)
    assert triangle.perimeter() == 15


def test_perimeter_isosceles():
    # Тест периметра равнобедренного треугольника
    triangle = Triangle(5, 5, 8)
    assert triangle.perimeter() == 18


def test_perimeter_nonequilateral():
    # Тест периметра разностороннего треугольника
    triangle = Triangle(3, 4, 5)
    assert triangle.perimeter() == 12


def test_perimeter_with_floats():
    # Тест периметра с числами с плавающей точкой
    triangle = Triangle(2.5, 3.5, 4.5)
    assert triangle.perimeter() == 10.5


# Комбинированные тесты
def test_triangle_type_and_perimeter():
    # Тест совместной работы методов
    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == "nonequilateral"
    assert triangle.perimeter() == 12


def test_isosceles_triangle_properties():
    # Тест свойств равнобедренного треугольника
    triangle = Triangle(6, 6, 10)
    assert triangle.triangle_type() == "isosceles"
    assert triangle.perimeter() == 22
    assert triangle.side1 == triangle.side2