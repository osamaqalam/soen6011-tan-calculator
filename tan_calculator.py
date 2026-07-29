#!/usr/bin/env python3
"""
tan_calculator.py — Tangent Function Calculator (From Scratch)
SOEN 6011, Problem 5: Implementation of tan(x) using only
                     arithmetic, input, output, and Tkinter.
Algorithm: Ratio via Taylor Series (sin(x) / cos(x))
No math library functions used.
"""

PI = 3.14159265358979323846
TOLERANCE = 1e-12
MAX_TERMS = 100


def abs_val(x: float) -> float:
    return x if x >= 0 else -x


def modulo(x: float, y: float) -> float:
    quotient = int(x / y)
    remainder = x - quotient * y
    if remainder < 0:
        remainder += y
    return remainder


def round_int(x: float) -> int:
    return int(x + 0.5) if x >= 0 else int(x - 0.5)


# ---------- core trigonometric functions ----------

def reduce_angle(x: float) -> float:
    two_pi = 2.0 * PI
    x = modulo(x, two_pi)
    return x


def sin_taylor(x: float) -> float:
    x = reduce_angle(x)
    result = 0.0
    term = x
    n = 1
    for _ in range(MAX_TERMS):
        result += term
        term *= -(x * x) / ((2 * n) * (2 * n + 1))
        if abs_val(term) < TOLERANCE:
            break
        n += 1
    return result


def cos_taylor(x: float) -> float:
    x = reduce_angle(x)
    result = 0.0
    term = 1.0
    n = 1
    for _ in range(MAX_TERMS):
        result += term
        term *= -(x * x) / ((2 * n - 1) * (2 * n))
        if abs_val(term) < TOLERANCE:
            break
        n += 1
    return result


def tan_ratio(x_rad: float) -> float | str:
    reduced = reduce_angle(x_rad)

    quotient = (reduced / PI) - 0.5
    if abs_val(quotient - round_int(quotient)) < 1e-12:
        k_val = round_int(quotient)
        return f"Undefined: asymptote at x = {x_rad:.6f} rad (x = pi/2 + {k_val}*pi)"

    sin_val = sin_taylor(reduced)
    cos_val = cos_taylor(reduced)
    return sin_val / cos_val


# ---------- TUI ----------

def degrees_to_radians(deg: float) -> float:
    return deg * (PI / 180.0)


def get_numeric_input(prompt: str) -> float:
    raw = input(prompt).strip()
    try:
        return float(raw)
    except ValueError:
        raise ValueError(f"Invalid input '{raw}': please enter a real number.")


def select_unit() -> str:
    while True:
        unit = input("Unit (deg/rad): ").strip().lower()
        if unit in ("deg", "rad"):
            return unit
        print("Invalid choice. Please enter 'deg' or 'rad'.")


def run():
    print("=" * 50)
    print("  TANGENT FUNCTION CALCULATOR — tan(x)")
    print("  SOEN 6011 | Algorithm: sin(x)/cos(x) via Taylor Series")
    print("=" * 50)

    while True:
        print()
        try:
            x_input = get_numeric_input("Enter angle: ")
            unit = select_unit()

            x_rad = degrees_to_radians(x_input) if unit == "deg" else x_input

            result = tan_ratio(x_rad)

            if isinstance(result, str):
                print(f"\n  {result}")
            else:
                print(f"\n  tan({x_input}) = {result:.10f}")
        except ValueError as e:
            print(f"\n  Error: {e}")
        except KeyboardInterrupt:
            print("\n\n  Goodbye.")
            break

        print()
        again = input("Compute another? (y/n): ").strip().lower()
        if again != "y":
            print("  Goodbye.")
            break


if __name__ == "__main__":
    run()
