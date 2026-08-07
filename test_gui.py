#!/usr/bin/env python3
"""
test_gui.py — Unit Tests for the Tkinter GUI
SOEN 6011, Problem 8
Framework: PyUnit (unittest)
"""

import unittest
import tkinter as tk
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tan_calculator import PI
from tan_calculator_gui import TanCalculatorApp


class TestGUI(unittest.TestCase):
    """Tests for the Tkinter GUI."""

    @classmethod
    def setUpClass(cls):
        cls.root = tk.Tk()
        cls.root.withdraw()
        cls.app = TanCalculatorApp(cls.root)

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

    def _get_output(self):
        return self.app.output.get("1.0", "end-1c")

    def test_tan_45_degrees(self):
        self.app.entry.delete(0, "end")
        self.app.entry.insert(0, "45")
        self.app.unit_var.set("deg")
        self.app.compute()
        self.assertIn("tan(45.0 deg)", self._get_output())
        self.assertIn("1.000000", self._get_output())

    def test_tan_90_degrees_asymptote(self):
        self.app.entry.delete(0, "end")
        self.app.entry.insert(0, "90")
        self.app.unit_var.set("deg")
        self.app.compute()
        self.assertIn("Undefined", self._get_output())
        self.assertIn("asymptote", self._get_output())

    def test_tan_180_degrees(self):
        self.app.entry.delete(0, "end")
        self.app.entry.insert(0, "180")
        self.app.unit_var.set("deg")
        self.app.compute()
        self.assertIn("0.000000", self._get_output())

    def test_empty_input(self):
        self.app.entry.delete(0, "end")
        self.app.entry.insert(0, "")
        self.app.compute()
        self.assertIn("Please enter", self._get_output())

    def test_invalid_input_text(self):
        self.app.entry.delete(0, "end")
        self.app.entry.insert(0, "abc")
        self.app.compute()
        self.assertIn("not a valid number", self._get_output())

    def test_negative_angle(self):
        self.app.entry.delete(0, "end")
        self.app.entry.insert(0, "-45")
        self.app.unit_var.set("deg")
        self.app.compute()
        self.assertIn("-1.000000", self._get_output())

    def test_radians_mode(self):
        self.app.entry.delete(0, "end")
        self.app.entry.insert(0, str(PI / 4))
        self.app.unit_var.set("rad")
        self.app.compute()
        self.assertIn("1.000000", self._get_output())

    def test_error_message_color(self):
        self.app.entry.delete(0, "end")
        self.app.entry.insert(0, "abc")
        self.app.compute()
        self.assertEqual(self.app.output.cget("fg"), "red")

    def test_success_message_color(self):
        self.app.entry.delete(0, "end")
        self.app.entry.insert(0, "45")
        self.app.unit_var.set("deg")
        self.app.compute()
        self.assertEqual(self.app.output.cget("fg"), "black")


if __name__ == "__main__":
    unittest.main(verbosity=2)
