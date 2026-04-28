# 🔢 Unit Converter

A clean, modular command-line unit converter built in Python. Supports 5 conversion categories with 57 total conversions, split across two files for easy maintenance and scalability.

---

## 📁 Project Structure

```
Python-Unit-Converter/
│
├── conversions.py    # All conversion dictionaries (data layer)
└── main.py           # Menus, logic, and program entry point
```

---

## ✨ Features

- **5 conversion categories** — Length, Time, Temperature, Weight, Speed
- **57 total conversions** across all categories
- **Modular design** — data separated from logic
- **Lambda functions** — every formula stored uniformly in dictionaries
- **Single reusable function** — `run_converter()` handles all categories
- **Continuous loop** — keeps running until the user chooses to exit

---

## 📦 Categories & Conversions

### 📏 Length (16 conversions)
| # | Conversion |
|---|---|
| 1 | Meter → Centimeter |
| 2 | Centimeter → Meter |
| 3 | Meter → Kilometer |
| 4 | Kilometer → Meter |
| 5 | Meter → Mile |
| 6 | Mile → Meter |
| 7 | Meter → Foot |
| 8 | Foot → Meter |
| 9 | Meter → Inch |
| 10 | Inch → Meter |
| 11 | Kilometer → Mile |
| 12 | Mile → Kilometer |
| 13 | Foot → Inch |
| 14 | Inch → Foot |
| 15 | Yard → Meter |
| 16 | Meter → Yard |

### ⏱️ Time (15 conversions)
| # | Conversion |
|---|---|
| 1 | Seconds → Minutes |
| 2 | Minutes → Hours |
| 3 | Hours → Days |
| 4 | Days → Years |
| 5 | Minutes → Seconds |
| 6 | Hours → Minutes |
| 7 | Days → Hours |
| 8 | Years → Days |
| 9 | Seconds → Hours |
| 10 | Seconds → Days |
| 11 | Minutes → Days |
| 12 | Weeks → Days |
| 13 | Days → Weeks |
| 14 | Milliseconds → Seconds |
| 15 | Seconds → Milliseconds |

### 🌡️ Temperature (6 conversions)
| # | Conversion |
|---|---|
| 1 | Celsius → Fahrenheit |
| 2 | Fahrenheit → Celsius |
| 3 | Celsius → Kelvin |
| 4 | Kelvin → Celsius |
| 5 | Fahrenheit → Kelvin |
| 6 | Kelvin → Fahrenheit |

### ⚖️ Weight (14 conversions)
| # | Conversion |
|---|---|
| 1 | Kilogram → Gram |
| 2 | Gram → Kilogram |
| 3 | Kilogram → Pound |
| 4 | Pound → Kilogram |
| 5 | Kilogram → Ounce |
| 6 | Ounce → Kilogram |
| 7 | Gram → Pound |
| 8 | Pound → Gram |
| 9 | Gram → Ounce |
| 10 | Ounce → Gram |
| 11 | Pound → Ounce |
| 12 | Ounce → Pound |
| 13 | Ton → Kilogram |
| 14 | Kilogram → Ton |

### 🚀 Speed (8 conversions)
| # | Conversion |
|---|---|
| 1 | km/h → m/s |
| 2 | m/s → km/h |
| 3 | km/h → mph |
| 4 | mph → km/h |
| 5 | m/s → mph |
| 6 | mph → m/s |
| 7 | Knot → km/h |
| 8 | km/h → Knot |

---

## ▶️ How to Run

**Requirements:** Python 3.13.6 (no external libraries needed)

1. Clone or download the project folder
2. Make sure both `main.py` and `conversions.py` are in the **same folder**
3. Open a terminal in that folder and run:

```bash
python main.py
```

---

## 🧠 How It Works

### `conversions.py`
Stores all conversion data as dictionaries. Each entry maps a choice number to a tuple of:
```python
choice_number: (lambda v: formula, "unit", "Label → Label")
```

### `main.py`
- Imports all dictionaries from `conversions.py`
- Defines a single `run_converter(title, menu, conversions)` function
- Uses a `while True` loop to keep the program running
- Calls `run_converter()` with the appropriate data based on the user's category choice

---

## 🔧 How to Add a New Conversion

**Step 1** — Add a new entry in `conversions.py`:
```python
# Example: adding Meter → Millimeter to length_conversions
17: (lambda v: v * 1000, "mm", "Meter → Millimeter"),
```

**Step 2** — Add it to the menu string in `main.py`:
```python
length_menu = """
    ...
    17: Meter → Millimeter"""
```

That's it — no other changes needed!

---

## 🔧 How to Add a New Category

**Step 1** — Add a new dictionary in `conversions.py`:
```python
area_conversions = {
    1: (lambda v: v * 10000, "cm²", "Meter² → Centimeter²"),
    ...
}
```

**Step 2** — Import it in `main.py`:
```python
from conversions import (..., area_conversions)
```

**Step 3** — Add a menu string and a new `elif` in the main loop:
```python
elif a == 6:
    run_converter("AREA CONVERTER", area_menu, area_conversions)
```

---

## 👤 Author

**Rajratna Dhiwar**  
Python Unit Converter Project
