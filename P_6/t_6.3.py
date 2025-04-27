import unittest
import sys

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorial(unittest.TestCase):
    def test_factorial_positive(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        self.assertRaises(ValueError, factorial, -1)

    def test_factorial_large(self):
        self.assertRaises(ValueError, factorial, 85)

    def test_factorial_edge(self):
        self.assertEqual(factorial(2), 2)

    def test_factorial_float(self):
        self.assertRaises(TypeError, factorial, 7.4)

unittest.main() 