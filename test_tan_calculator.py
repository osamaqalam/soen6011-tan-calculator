#!/usr/bin/env python3
"""
test_tan_calculator.py — Unit Tests for tan(x) Calculator
SOEN 6011, Problem 8
Framework: PyUnit (unittest)
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tan_calculator import (
    PI,
    abs_val,
    modulo,
    round_int,
    reduce_angle,
    sin_taylor,
    cos_taylor,
    tan_ratio,
)


class TestSubordinateFunctions(unittest.TestCase):
    """Tests for hand-written subordinate functions."""

    def test_abs_positive(self):
        self.assertEqual(abs_val(5.0), 5.0)

    def test_abs_negative(self):
        self.assertEqual(abs_val(-3.14), 3.14)

    def test_abs_zero(self):
        self.assertEqual(abs_val(0.0), 0.0)

    def test_modulo_basic(self):
        self.assertAlmostEqual(modulo(7.0, 3.0), 1.0)

    def test_modulo_negative_dividend(self):
        self.assertAlmostEqual(modulo(-1.0, 3.0), 2.0)

    def test_modulo_zero(self):
        self.assertAlmostEqual(modulo(6.0, 3.0), 0.0)

    def test_round_int_positive_up(self):
        self.assertEqual(round_int(3.7), 4)

    def test_round_int_positive_down(self):
        self.assertEqual(round_int(3.2), 3)

    def test_round_int_negative_up(self):
        self.assertEqual(round_int(-3.2), -3)

    def test_round_int_negative_down(self):
        self.assertEqual(round_int(-3.7), -4)

    def test_pi_value(self):
        self.assertAlmostEqual(PI, 3.141592653589793, places=12)


class TestReduceAngle(unittest.TestCase):
    """Tests for range reduction to [0, 2*pi)."""

    def test_within_range(self):
        self.assertAlmostEqual(reduce_angle(1.0), 1.0)

    def test_above_range(self):
        two_pi = 2.0 * PI
        self.assertAlmostEqual(reduce_angle(two_pi + 1.0), 1.0)

    def test_negative_angle(self):
        two_pi = 2.0 * PI
        self.assertAlmostEqual(reduce_angle(-1.0), two_pi - 1.0)


class TestSinCosTaylor(unittest.TestCase):
    """Tests for sin(x) and cos(x) via Taylor series."""

    def test_sin_zero(self):
        self.assertAlmostEqual(sin_taylor(0.0), 0.0, places=10)

    def test_sin_pi_over_2(self):
        self.assertAlmostEqual(sin_taylor(PI / 2.0), 1.0, places=10)

    def test_sin_pi(self):
        self.assertAlmostEqual(sin_taylor(PI), 0.0, places=10)

    def test_sin_negative(self):
        self.assertAlmostEqual(sin_taylor(-PI / 2.0), -1.0, places=10)

    def test_cos_zero(self):
        self.assertAlmostEqual(cos_taylor(0.0), 1.0, places=10)

    def test_cos_pi_over_2(self):
        self.assertAlmostEqual(cos_taylor(PI / 2.0), 0.0, places=8)

    def test_cos_pi(self):
        self.assertAlmostEqual(cos_taylor(PI), -1.0, places=10)


class TestTanRatio(unittest.TestCase):
    """Tests for tan(x) = sin(x)/cos(x)."""

    def test_tan_zero(self):
        self.assertAlmostEqual(tan_ratio(0.0), 0.0, places=10)

    def test_tan_45_degrees(self):
        x = 45.0 * PI / 180.0
        self.assertAlmostEqual(tan_ratio(x), 1.0, places=10)

    def test_tan_60_degrees(self):
        x = 60.0 * PI / 180.0
        self.assertAlmostEqual(tan_ratio(x), 1.73205080757, places=8)

    def test_tan_30_degrees(self):
        x = 30.0 * PI / 180.0
        expected = 1.0 / (3.0 ** 0.5)
        self.assertAlmostEqual(tan_ratio(x), expected, places=8)

    def test_tan_180_degrees(self):
        x = 180.0 * PI / 180.0
        self.assertAlmostEqual(tan_ratio(x), 0.0, places=10)

    def test_tan_negative_45_degrees(self):
        x = -45.0 * PI / 180.0
        self.assertAlmostEqual(tan_ratio(x), -1.0, places=10)

    def test_tan_near_90_from_left(self):
        x = 89.999 * PI / 180.0
        result = tan_ratio(x)
        self.assertIsInstance(result, float)
        self.assertGreater(result, 50000)

    def test_tan_pi(self):
        self.assertAlmostEqual(tan_ratio(PI), 0.0, places=10)


class TestTanAsymptotes(unittest.TestCase):
    """Tests for asymptote detection at x = pi/2 + k*pi."""

    def test_asymptote_90_degrees(self):
        x = 90.0 * PI / 180.0
        result = tan_ratio(x)
        self.assertIsInstance(result, str)
        self.assertIn("Undefined", result)

    def test_asymptote_270_degrees(self):
        x = 270.0 * PI / 180.0
        result = tan_ratio(x)
        self.assertIsInstance(result, str)
        self.assertIn("Undefined", result)

    def test_asymptote_negative_90_degrees(self):
        x = -90.0 * PI / 180.0
        result = tan_ratio(x)
        self.assertIsInstance(result, str)
        self.assertIn("Undefined", result)

    def test_asymptote_450_degrees(self):
        x = 450.0 * PI / 180.0
        result = tan_ratio(x)
        self.assertIsInstance(result, str)
        self.assertIn("Undefined", result)

    def test_not_asymptote_89_degrees(self):
        x = 89.0 * PI / 180.0
        result = tan_ratio(x)
        self.assertIsInstance(result, float)


class TestTanProperty(unittest.TestCase):
    """Tests for mathematical properties of tan(x)."""

    def test_odd_function(self):
        x = 1.0
        self.assertAlmostEqual(tan_ratio(-x), -tan_ratio(x), places=10)

    def test_period_pi(self):
        x = 0.5
        self.assertAlmostEqual(tan_ratio(x + PI), tan_ratio(x), places=10)

    def test_tan_equals_sin_over_cos(self):
        x = 0.7
        expected = sin_taylor(x) / cos_taylor(x)
        self.assertAlmostEqual(tan_ratio(x), expected, places=10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
