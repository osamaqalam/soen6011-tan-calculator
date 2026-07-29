# soen6011-tan-calculator

A scientific calculator implementation of the transcendental function **tan(x)** — built for SOEN 6011 (Software Engineering Processes) at Concordia University.

## How to Run

### GUI (Graphical User Interface)

```bash
python tan_calculator_gui.py
```

- Enter an angle and select the unit (degrees or radians)
- Press the **Compute tan(x)** button or hit **Enter**
- The result is displayed in the output area
- Error messages appear in red with suggestions on how to fix them

**Requirements:** Python 3.x with tkinter (included in standard Python distribution).

### TUI (Textual User Interface)

```bash
python tan_calculator.py
```

- Follow the command-line prompts to enter the angle and unit

## Algorithm

tan(x) is computed as **sin(x) / cos(x)** using Taylor series expansions.

### Sine (Taylor Series)

```
sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + ...
```

### Cosine (Taylor Series)

```
cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ...
```

**Optimizations:**
- **Range reduction:** Input is reduced to [0, 2π) before computation
- **Recurrence-based iteration:** Terms are computed incrementally — no factorial calls per iteration
- **Early exit:** Loop breaks when a term's absolute value falls below tolerance (10⁻¹²)
- **Asymptote detection:** Uses a mathematical proximity check: |x/π − 0.5 − k| < 10⁻¹²

### Asymptote Handling

tan(x) is undefined at x = π/2 + kπ (where k is any integer). The function detects these values mathematically rather than relying on floating-point cos(x) ≈ 0, which avoids precision issues at exactly 90°, 270°, etc.

## Requirements Traceability

| ID | Requirement | Implementation |
|---|---|---|
| FR-01 | Accept real number input | `float()` parsing in GUI entry and TUI prompt |
| FR-02 | Select degrees or radians | Radio buttons (GUI), prompt (TUI) |
| FR-03 | Compute tan(x) = sin(x)/cos(x) | `tan_ratio()` → `sin_taylor()` / `cos_taylor()` |
| FR-04 | Detect asymptotes (π/2 + kπ) | Mathematical proximity check in `tan_ratio()` |
| FR-05 | Display descriptive error messages | `set_output(text, is_error=True)` — red color |
| FR-06 | Display at least 6 decimal places | Formatted to 10 decimal places |
| FR-07 | Reject non-numeric input | `ValueError` catch with helpful message |
| FR-08 | Allow repeated computations | Persistent GUI window, TUI loop |

## Files

| File | Description |
|---|---|
| `tan_calculator.py` | Core implementation — Taylor series, tan computation, TUI |
| `tan_calculator_gui.py` | Tkinter GUI wrapping the core functions |
| `README.md` | This file |

## License

This project is developed for academic purposes as part of SOEN 6011 at Concordia University.
