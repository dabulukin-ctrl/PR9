import unittest
from PR9.LR6 import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-4, 5), 1)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(0, 0)

    def test_is_prime_number(self):
        self.assertEqual(self.calc.is_prime_number(1),False)
        self.assertEqual(self.calc.is_prime_number(15), False)
        self.assertEqual(self.calc.is_prime_number(7), True)


if __name__ == '__main__':

    unittest.main()
