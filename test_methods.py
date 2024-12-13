import unittest
import math
from operations import add, subtract, multiply, divide, remainder, sin, cos, power, square_root, floor, ceil
from memory import memory_add, memory_clear, memory_recall

class TestMathOperations(unittest.TestCase):

    # Тесты для арифметических операций
    def test_add(self):
        test_cases = [
            (1, 2, 3),
            (-1, 1, 0),
            (-1, -1, -2),
            (0, 0, 0),
            (100, 200, 300)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)

    def test_subtract(self):
        test_cases = [
            (5, 3, 2),
            (3, 5, -2),
            (0, 0, 0),
            (10, 5, 5),
            (-5, -5, 0)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(subtract(a, b), expected)

    def test_multiply(self):
        test_cases = [
            (3, 4, 12),
            (0, 5, 0),
            (-2, 3, -6),
            (7, -8, -56),
            (-3, -3, 9)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(multiply(a, b), expected)

    def test_divide(self):
        test_cases = [
            (6, 3, 2),
            (5, 2, 2.5),
            (-10, 2, -5),
            (7, -1, -7)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(divide(a, b), expected)
        # Тест деления на ноль
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_remainder(self):
        test_cases = [
            (5, 2, 1),
            (6, 3, 0),
            (10, 4, 2),
            (-5, 2, -1)  # Исправленный ожидаемый результат
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(remainder(a, b), expected)
        # Тест остатка от деления на ноль
        with self.assertRaises(ValueError):
            remainder(1, 0)

    # Тесты для тригонометрических функций
    def test_sin(self):
        test_cases = [
            (0, 0),
            (30, 0.5),
            (90, 1),
            (180, 0),
            (270, -1),
            (360, 0)
        ]
        for angle, expected in test_cases:
            with self.subTest(angle=angle):
                self.assertAlmostEqual(sin(angle), expected, places=5)

    def test_cos(self):
        test_cases = [
            (0, 1),
            (30, math.sqrt(3)/2),
            (90, 0),
            (180, -1),
            (270, 0),
            (360, 1)
        ]
        for angle, expected in test_cases:
            with self.subTest(angle=angle):
                self.assertAlmostEqual(cos(angle), expected, places=5)

    # Тесты для возведения в степень
    def test_power(self):
        test_cases = [
            (2, 3, 8),
            (5, 0, 1),
            (2, -1, 0.5),
            (3, 4, 81),
            (-2, 3, -8)
        ]
        for base, exponent, expected in test_cases:
            with self.subTest(base=base, exponent=exponent):
                self.assertEqual(power(base, exponent), expected)

    # Тесты для квадратного корня
    def test_square_root(self):
        test_cases = [
            (9, 3),
            (0, 0),
            (16, 4),
            (25, 5)
        ]
        for value, expected in test_cases:
            with self.subTest(value=value):
                self.assertEqual(square_root(value), expected)
        # Тест квадратного корня из отрицательного числа
        with self.assertRaises(ValueError):
            square_root(-1)

    # Тесты для округления
    def test_floor(self):
        test_cases = [
            (3.7, 3),
            (-3.7, -4),
            (0, 0),
            (2.0, 2),
            (-2.1, -3)
        ]
        for value, expected in test_cases:
            with self.subTest(value=value):
                self.assertEqual(floor(value), expected)

    def test_ceil(self):
        test_cases = [
            (3.1, 4),
            (-3.1, -3),
            (0, 0),
            (2.0, 2),
            (-2.9, -2)
        ]
        for value, expected in test_cases:
            with self.subTest(value=value):
                self.assertEqual(ceil(value), expected)

    # Тесты для памяти
    def test_memory_add_and_recall(self):
        memory_clear()
        memory_add(10)
        self.assertEqual(memory_recall(), 10)
        memory_add(5)
        self.assertEqual(memory_recall(), 15)

    def test_memory_clear(self):
        memory_add(100)
        memory_clear()
        self.assertEqual(memory_recall(), 0)

    def test_memory_recall(self):
        memory_clear()
        memory_add(100)
        self.assertEqual(memory_recall(), 100)
        memory_add(50)
        self.assertEqual(memory_recall(), 150)
        memory_clear()
        self.assertEqual(memory_recall(), 0)

if __name__ == "__main__":
    unittest.main()
