# test_math.py
# Tester: Kristian
# Tests for: factorial, floor, area_of_circle, is_perfect_number

import unittest
from my_math import factorial, floor, area_of_circle, is_perfect_number


class TestFactorial(unittest.TestCase):

    # Typical cases
    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_10(self):
        self.assertEqual(factorial(10), 3628800)

    # Edge cases
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    # Invalid input
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_factorial_float(self):
        with self.assertRaises(TypeError):
            factorial(3.5)

    def test_factorial_string(self):
        with self.assertRaises(TypeError):
            factorial("five")


class TestFloor(unittest.TestCase):

    # Typical cases
    def test_floor_positive_float(self):
        self.assertEqual(floor(3.7), 3)

    def test_floor_negative_float(self):
        self.assertEqual(floor(-2.3), -3)

    def test_floor_whole_number(self):
        self.assertEqual(floor(5.0), 5)

    # Edge cases
    def test_floor_zero(self):
        self.assertEqual(floor(0), 0)

    def test_floor_negative_whole(self):
        self.assertEqual(floor(-4.0), -4)

    # Invalid input
    def test_floor_string(self):
        with self.assertRaises(TypeError):
            floor("three")

    def test_floor_none(self):
        with self.assertRaises(TypeError):
            floor(None)


class TestAreaOfCircle(unittest.TestCase):

    # Typical cases
    def test_area_radius_1(self):
        self.assertAlmostEqual(area_of_circle(1), 3.141592653589793)

    def test_area_radius_5(self):
        self.assertAlmostEqual(area_of_circle(5), 78.53981633974483)

    def test_area_radius_float(self):
        self.assertAlmostEqual(area_of_circle(2.5), 19.634954084936208)

    # Edge cases
    def test_area_radius_zero(self):
        self.assertEqual(area_of_circle(0), 0)

    # Invalid input
    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            area_of_circle(-1)

    def test_area_string_input(self):
        with self.assertRaises(TypeError):
            area_of_circle("r")

    def test_area_none_input(self):
        with self.assertRaises(TypeError):
            area_of_circle(None)


class TestIsPerfectNumber(unittest.TestCase):

    # Typical cases
    def test_perfect_6(self):
        self.assertTrue(is_perfect_number(6))

    def test_perfect_28(self):
        self.assertTrue(is_perfect_number(28))

    def test_not_perfect_10(self):
        self.assertFalse(is_perfect_number(10))

    # Edge cases
    def test_perfect_1(self):
        self.assertFalse(is_perfect_number(1))

    def test_perfect_496(self):
        self.assertTrue(is_perfect_number(496))

    # Invalid input
    def test_perfect_negative(self):
        with self.assertRaises(ValueError):
            is_perfect_number(-5)

    def test_perfect_float(self):
        with self.assertRaises(TypeError):
            is_perfect_number(6.0)

    def test_perfect_string(self):
        with self.assertRaises(TypeError):
            is_perfect_number("six")


if __name__ == "__main__":
    unittest.main()