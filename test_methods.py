import unittest
import math
from operations import add, subtract, multiply, divide, remainder, sin, cos, power, square_root, floor, ceil
from memory import memory_add, memory_clear, memory_recall

class TestMathOperations(unittest.TestCase):

    # Тесты для арифметических операций
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_remainder(self):
        self.assertEqual(remainder(5, 2), 1)
        self.assertEqual(remainder(6, 3), 0)
        with self.assertRaises(ValueError):
            remainder(1, 0)

    # Тесты для тригонометрических функций
    def test_sin(self):
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(30), 0.5)
        self.assertAlmostEqual(sin(90), 1)

    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(30), math.sqrt(3)/2)
        self.assertAlmostEqual(cos(90), 0)

    # Тесты для возведения в степень
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -1), 0.5)

    # Тесты для квадратного корня
    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-1)

    # Тесты для округления
    def test_floor(self):
        self.assertEqual(floor(3.7), 3)
        self.assertEqual(floor(-3.7), -4)
        self.assertEqual(floor(0), 0)

    def test_ceil(self):
        self.assertEqual(ceil(3.1), 4)
        self.assertEqual(ceil(-3.1), -3)
        self.assertEqual(ceil(0), 0)

    # Тесты для памяти
    def test_memory_add(self):
        memory_clear()
        memory_add(10)
        self.assertEqual(memory_recall(), 10)
        memory_add(5)
        self.assertEqual(memory_recall(), 15)

    def test_memory_clear(self):
        memory_clear()
        self.assertEqual(memory_recall(), 0)

    def test_memory_recall(self):
        memory_clear()
        memory_add(100)
        self.assertEqual(memory_recall(), 100)
        memory_clear()
        self.assertEqual(memory_recall(), 0)

if __name__ == "__main__":
    unittest.main()
