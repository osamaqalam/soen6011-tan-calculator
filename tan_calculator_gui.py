#!/usr/bin/env python3
"""
tan_calculator_gui.py — Tangent Function Calculator (with GUI)
SOEN 6011, Problem 5
Uses tan_ratio() from tan_calculator.py (D1/Problem 4 implementation).
"""

import tkinter as tk
from tkinter import messagebox
import math
from tan_calculator import tan_ratio


class TanCalculatorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("tan(x) Calculator — SOEN 6011")
        root.resizable(False, False)

        pad = {"padx": 12, "pady": 6}

        tk.Label(root, text="tan(x) Calculator",
                 font=("Helvetica", 14, "bold")).grid(row=0, column=0,
                                                       columnspan=2, **pad)

        tk.Label(root, text="Angle:").grid(row=1, column=0, sticky="e", **pad)
        self.entry = tk.Entry(root, width=20, font=("Courier", 12))
        self.entry.grid(row=1, column=1, sticky="w", **pad)
        self.entry.bind("<Return>", lambda e: self.compute())
        self.entry.focus_set()

        self.unit_var = tk.StringVar(value="deg")
        tk.Label(root, text="Unit:").grid(row=2, column=0, sticky="e", **pad)
        frame_units = tk.Frame(root)
        frame_units.grid(row=2, column=1, sticky="w", **pad)
        tk.Radiobutton(frame_units, text="Degrees", variable=self.unit_var,
                       value="deg").pack(side="left")
        tk.Radiobutton(frame_units, text="Radians", variable=self.unit_var,
                       value="rad").pack(side="left")

        self.btn = tk.Button(root, text="Compute tan(x)", width=18,
                             command=self.compute,
                             font=("Helvetica", 10, "bold"))
        self.btn.grid(row=3, column=0, columnspan=2, **pad)

        self.output = tk.Text(root, width=40, height=3, font=("Courier", 11),
                              state="disabled", bg="#f5f5f5", relief="sunken")
        self.output.grid(row=4, column=0, columnspan=2, **pad)

    def set_output(self, text: str, is_error: bool = False):
        self.output.config(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", text)
        if is_error:
            self.output.config(fg="red")
        else:
            self.output.config(fg="black")
        self.output.config(state="disabled")

    def compute(self):
        raw = self.entry.get().strip()

        if raw == "":
            self.set_output(
                "Please enter an angle value.\n"
                "Example: 45 or 1.5708",
                is_error=True)
            return

        try:
            angle = float(raw)
        except ValueError:
            self.set_output(
                f"'{raw}' is not a valid number.\n"
                "Please enter a real number (e.g., 45, -30.5, 1.5708).",
                is_error=True)
            return

        unit = self.unit_var.get()
        try:
            x_rad = angle * (math.pi / 180.0) if unit == "deg" else angle
        except Exception:
            self.set_output(
                "Error converting angle.\n"
                "Please check the unit selection and try again.",
                is_error=True)
            return

        try:
            result = tan_ratio(x_rad)
        except ZeroDivisionError:
            self.set_output(
                "Math error: division by zero.\n"
                "The input may be at an asymptote (x = pi/2 + k*pi).",
                is_error=True)
            return
        except Exception as exc:
            self.set_output(
                f"Unexpected error during computation:\n{exc}\n"
                "Please try a different angle value.",
                is_error=True)
            return

        unit_str = "deg" if unit == "deg" else "rad"
        if isinstance(result, str):
            self.set_output(result, is_error=True)
        else:
            self.set_output(f"tan({angle} {unit_str}) =\n{result:.10f}")


def main():
    root = tk.Tk()
    TanCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
