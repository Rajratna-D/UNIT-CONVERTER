# This is the main file for the unit converter
# All conversion data is imported from conversions.py

from conversions import (
    length_conversions,
    time_conversions,
    temperature_conversions,
    weight_conversions,
    speed_conversions
)

# all converters have the same logic 
def run_converter(title, menu, conversions):
    print(f"\n {title} ")
    print(menu)
    choice = int(input("Enter your choice: "))
    value = float(input("Enter your value: "))

    if choice in conversions:
        formula, unit, label = conversions[choice]
        print(f"{label} = {round(formula(value), 4)} {unit}")
    else:
        print("Invalid choice!")



length_menu = """
    1:  Meter       → Centimeter      9:  Meter       → Inch
    2:  Centimeter  → Meter           10: Inch        → Meter
    3:  Meter       → Kilometer       11: Kilometer   → Mile
    4:  Kilometer   → Meter           12: Mile        → Kilometer
    5:  Meter       → Mile            13: Foot        → Inch
    6:  Mile        → Meter           14: Inch        → Foot
    7:  Meter       → Foot            15: Yard        → Meter
    8:  Foot        → Meter           16: Meter       → Yard"""

time_menu = """
    1:  Seconds      → Minutes        9:  Seconds      → Hours
    2:  Minutes      → Hours          10: Seconds      → Days
    3:  Hours        → Days           11: Minutes      → Days
    4:  Days         → Years          12: Weeks        → Days
    5:  Minutes      → Seconds        13: Days         → Weeks
    6:  Hours        → Minutes        14: Milliseconds → Seconds
    7:  Days         → Hours          15: Seconds      → Milliseconds
    8:  Years        → Days"""

temperature_menu = """
    1: Celsius    → Fahrenheit
    2: Fahrenheit → Celsius
    3: Celsius    → Kelvin
    4: Kelvin     → Celsius
    5: Fahrenheit → Kelvin
    6: Kelvin     → Fahrenheit"""

weight_menu = """
    1:  Kilogram  → Gram             8:  Pound     → Gram
    2:  Gram      → Kilogram         9:  Gram      → Ounce
    3:  Kilogram  → Pound            10: Ounce     → Gram
    4:  Pound     → Kilogram         11: Pound     → Ounce
    5:  Kilogram  → Ounce            12: Ounce     → Pound
    6:  Ounce     → Kilogram         13: Ton       → Kilogram
    7:  Gram      → Pound            14: Kilogram  → Ton"""

speed_menu = """
    1: km/h  → m/s           5: m/s   → mph
    2: m/s   → km/h          6: mph   → m/s
    3: km/h  → mph           7: Knot  → km/h
    4: mph   → km/h          8: km/h  → Knot"""


# Main loop/codeblock 
while True:
    print("""  UNIT CONVERTER

  1: Length
  2: Time
  3: Temperature
  4: Weight
  5: Speed
  0: Exit
""")

    a = int(input("Enter your choice: "))

    if a == 1:
        run_converter("LENGTH CONVERTER", length_menu, length_conversions)
    elif a == 2:
        run_converter("TIME CONVERTER", time_menu, time_conversions)
    elif a == 3:
        run_converter("TEMPERATURE CONVERTER", temperature_menu, temperature_conversions)
    elif a == 4:
        run_converter("WEIGHT CONVERTER", weight_menu, weight_conversions)
    elif a == 5:
        run_converter("SPEED CONVERTER", speed_menu, speed_conversions)
    elif a == 0:
        print("\nThank you for using the Unit Converter. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")