# This file contains all the conversion dictionaries for the unit converter

length_conversions = {
    1:  (lambda v: v * 100,         "cm",  "Meter → Centimeter"),
    2:  (lambda v: v / 100,         "m",   "Centimeter → Meter"),
    3:  (lambda v: v / 1000,        "km",  "Meter → Kilometer"),
    4:  (lambda v: v * 1000,        "m",   "Kilometer → Meter"),
    5:  (lambda v: v / 1609.344,    "mi",  "Meter → Mile"),
    6:  (lambda v: v * 1609.344,    "m",   "Mile → Meter"),
    7:  (lambda v: v * 3.28084,     "ft",  "Meter → Foot"),
    8:  (lambda v: v / 3.28084,     "m",   "Foot → Meter"),
    9:  (lambda v: v * 39.3701,     "in",  "Meter → Inch"),
    10: (lambda v: v / 39.3701,     "m",   "Inch → Meter"),
    11: (lambda v: v / 1.60934,     "mi",  "Kilometer → Mile"),
    12: (lambda v: v * 1.60934,     "km",  "Mile → Kilometer"),
    13: (lambda v: v * 12,          "in",  "Foot → Inch"),
    14: (lambda v: v / 12,          "ft",  "Inch → Foot"),
    15: (lambda v: v * 0.9144,      "m",   "Yard → Meter"),
    16: (lambda v: v / 0.9144,      "yd",  "Meter → Yard"),
}

time_conversions = {
    1:  (lambda v: v / 60,      "min",  "Seconds → Minutes"),
    2:  (lambda v: v / 60,      "hrs",  "Minutes → Hours"),
    3:  (lambda v: v / 24,      "days", "Hours → Days"),
    4:  (lambda v: v / 365,     "yrs",  "Days → Years"),
    5:  (lambda v: v * 60,      "sec",  "Minutes → Seconds"),
    6:  (lambda v: v * 60,      "min",  "Hours → Minutes"),
    7:  (lambda v: v * 24,      "hrs",  "Days → Hours"),
    8:  (lambda v: v * 365,     "days", "Years → Days"),
    9:  (lambda v: v / 3600,    "hrs",  "Seconds → Hours"),
    10: (lambda v: v / 86400,   "days", "Seconds → Days"),
    11: (lambda v: v / 1440,    "days", "Minutes → Days"),
    12: (lambda v: v * 7,       "days", "Weeks → Days"),
    13: (lambda v: v / 7,       "wks",  "Days → Weeks"),
    14: (lambda v: v / 1000,    "sec",  "Milliseconds → Seconds"),
    15: (lambda v: v * 1000,    "ms",   "Seconds → Milliseconds"),
}

temperature_conversions = {
    1: (lambda v: (v * 9/5) + 32,           "°F", "Celsius → Fahrenheit"),
    2: (lambda v: (v - 32) * 5/9,           "°C", "Fahrenheit → Celsius"),
    3: (lambda v: v + 273.15,               "K",  "Celsius → Kelvin"),
    4: (lambda v: v - 273.15,               "°C", "Kelvin → Celsius"),
    5: (lambda v: (v - 32) * 5/9 + 273.15, "K",  "Fahrenheit → Kelvin"),
    6: (lambda v: (v - 273.15) * 9/5 + 32, "°F", "Kelvin → Fahrenheit"),
}

weight_conversions = {
    1:  (lambda v: v * 1000,     "g",   "Kilogram → Gram"),
    2:  (lambda v: v / 1000,     "kg",  "Gram → Kilogram"),
    3:  (lambda v: v * 2.20462,  "lb",  "Kilogram → Pound"),
    4:  (lambda v: v / 2.20462,  "kg",  "Pound → Kilogram"),
    5:  (lambda v: v * 35.274,   "oz",  "Kilogram → Ounce"),
    6:  (lambda v: v / 35.274,   "kg",  "Ounce → Kilogram"),
    7:  (lambda v: v / 453.592,  "lb",  "Gram → Pound"),
    8:  (lambda v: v * 453.592,  "g",   "Pound → Gram"),
    9:  (lambda v: v / 28.3495,  "oz",  "Gram → Ounce"),
    10: (lambda v: v * 28.3495,  "g",   "Ounce → Gram"),
    11: (lambda v: v * 16,       "oz",  "Pound → Ounce"),
    12: (lambda v: v / 16,       "lb",  "Ounce → Pound"),
    13: (lambda v: v * 1000,     "kg",  "Ton → Kilogram"),
    14: (lambda v: v / 1000,     "ton", "Kilogram → Ton"),
}

speed_conversions = {
    1: (lambda v: v / 3.6,       "m/s",  "km/h → m/s"),
    2: (lambda v: v * 3.6,       "km/h", "m/s → km/h"),
    3: (lambda v: v / 1.60934,   "mph",  "km/h → mph"),
    4: (lambda v: v * 1.60934,   "km/h", "mph → km/h"),
    5: (lambda v: v * 2.23694,   "mph",  "m/s → mph"),
    6: (lambda v: v / 2.23694,   "m/s",  "mph → m/s"),
    7: (lambda v: v * 1.852,     "km/h", "Knot → km/h"),
    8: (lambda v: v / 1.852,     "kn",   "km/h → Knot"),
}