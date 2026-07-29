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

    def set_output(self, text: str):
        self.output.config(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", text)
        self.output.config(state="disabled")

    def compute(self):
        raw = self.entry.get().strip()
        try:
            angle = float(raw)
        except ValueError:
            self.set_output(f"Invalid input '{raw}'. Please enter a number.")
            return

        unit = self.unit_var.get()
        x_rad = angle * (math.pi / 180.0) if unit == "deg" else angle

        result = tan_ratio(x_rad)
        unit_str = "deg" if unit == "deg" else "rad"
        self.set_output(f"tan({angle} {unit_str}) =\n{result}")


def main():
    root = tk.Tk()
    TanCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
