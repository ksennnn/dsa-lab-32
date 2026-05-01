import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestGetTriangleType(unittest.TestCase):
    
    # Позитивные тесты
    def test_equilateral_triangle(self):
        # Тест равностороннего треугольника
        result = get_triangle_type(3, 3, 3)
        self.assertEqual(result, "equilateral")
    
    def test_isosceles_triangle(self):
        # Тест равнобедренного треугольника
        result = get_triangle_type(5, 5, 8)
        self.assertEqual(result, "isosceles")
    
    def test_nonequilateral_triangle(self):
        # Тест разностороннего треугольника
        result = get_triangle_type(3, 4, 5)
        self.assertEqual(result, "nonequilateral")
    
    def test_isosceles_other_combination(self):
        # Тест равнобедренного треугольника с другой комбинацией сторон
        result = get_triangle_type(6, 10, 6)
        self.assertEqual(result, "isosceles")
    
    def test_large_numbers(self):
        # Тест с большими числами
        result = get_triangle_type(100, 150, 200)
        self.assertEqual(result, "nonequilateral")
    
    def test_float_sides_valid(self):
        # Тест с плавающей точкой - корректный треугольник
        result = get_triangle_type(2.5, 3.5, 4.5)
        self.assertEqual(result, "nonequilateral")
    
    # Негативные тесты
    def test_zero_side(self):
        # Тест с нулевой стороной
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 4, 5)
    
    def test_negative_side(self):
        # Тест с отрицательной стороной
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-3, 4, 5)
    
    def test_inequality_violation_less(self):
        # Тест нарушения неравенства треугольника (сумма меньше третьей)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 3)
    
    def test_inequality_violation_equal(self):
        # Тест нарушения неравенства треугольника (сумма равна третьей)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(2, 3, 5)
    
    def test_two_zero_sides(self):
        # Тест с двумя нулевыми сторонами
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 0, 5)
    
    def test_all_zero_sides(self):
        # Тест с всеми нулевыми сторонами
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 0, 0)
    
    def test_all_negative_sides(self):
        # Тест с отрицательными сторонами
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, -1, -1)
    
    def test_float_sides_invalid(self):
        # Тест с плавающей точкой - некорректный треугольник
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0.5, 0.5, 2.0)


if __name__ == '__main__':
    unittest.main()