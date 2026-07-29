#!/usr/bin/env python3
"""
tan_calculator.py — Tangent Function Calculator
SOEN 6011, Problem 4: Implementation of tan(x)
Algorithm: Ratio via Taylor Series (sin(x) / cos(x))
"""

import math

TOLERANCE = 1e-12
MAX_TERMS = 100
EPSILON = 1e-10


def reduce_angle(x: float) -> float:
    """Reduce angle to [0, 2*pi) using mathematical range reduction."""
    two_pi = 2.0 * math.pi
    x = x % two_pi
    if x < 0:
        x += two_pi
    return x


def sin_taylor(x: float) -> float:
    """Compute sin(x) using Taylor series expansion."""
    x = reduce_angle(x)
    result = 0.0
    term = x
    n = 1
    for _ in range(MAX_TERMS):
        result += term
        term *= -(x * x) / ((2 * n) * (2 * n + 1))
        if abs(term) < TOLERANCE:
            break
        n += 1
    return result


def cos_taylor(x: float) -> float:
    """Compute cos(x) using Taylor series expansion."""
    x = reduce_angle(x)
    result = 0.0
    term = 1.0
    n = 1
    for _ in range(MAX_TERMS):
        result += term
        term *= -(x * x) / ((2 * n - 1) * (2 * n))
        if abs(term) < TOLERANCE:
            break
        n += 1
    return result


def tan_ratio(x_rad: float) -> float | str:
    """
    Compute tan(x) = sin(x) / cos(x) using Taylor series for both.
    Returns float result or an error string if asymptote is detected.
    """
    reduced = reduce_angle(x_rad)

    quotient = (reduced / math.pi) - 0.5
    if abs(quotient - round(quotient)) < 1e-12:
        k = round(quotient)
        return f"Undefined: asymptote at x = {x_rad:.6f} rad (x = pi/2 + {k}*pi)"

    sin_val = sin_taylor(reduced)
    cos_val = cos_taylor(reduced)
    return sin_val / cos_val


def degrees_to_radians(deg: float) -> float:
    """Convert degrees to radians."""
    return deg * (math.pi / 180.0)


def get_numeric_input(prompt: str) -> float:
    """Prompt user for a numeric value; raise ValueError on non-numeric input."""
    raw = input(prompt).strip()
    try:
        return float(raw)
    except ValueError:
        raise ValueError(f"Invalid input '{raw}': please enter a real number.")


def select_unit() -> str:
    """Prompt user to select angle unit; returns 'deg' or 'rad'."""
    while True:
        unit = input("Unit (deg/rad): ").strip().lower()
        if unit in ("deg", "rad"):
            return unit
        print("Invalid choice. Please enter 'deg' or 'rad'.")


def run():
    """Main textual user interface loop."""
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
