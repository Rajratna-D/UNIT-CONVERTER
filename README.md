# Unit Converter

A simple yet powerful command-line unit converter written in Python. Convert between units of Length, Time, and Temperature with ease.

---

# Table of Contents

- [About](#about)
- [Features](#features)
- [Supported Conversions](#supported-conversions)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

##  About

**Unit Converter** is a beginner-friendly Python CLI application that allows users to perform common unit conversions across three categories: Length, Time, and Temperature. The program runs in a continuous loop, letting users perform multiple conversions in a single session without restarting.

---

## Features

- Continuous loop — convert as many values as you want in one session
- Length conversions
- Time conversions
- Temperature conversions
- Input validation with informative error messages
- Clean and minimal terminal interface

---

##  Supported Conversions

### Length
| # | Conversion |
|---|-----------|
| 1 | Meter → Centimeter |
| 2 | Centimeter → Meter |

### Time
| # | Conversion |
|---|-----------|
| 1 | Seconds → Minutes |
| 2 | Minutes → Hours |
| 3 | Hours → Days |
| 4 | Days → Years |

### Temperature
| # | Conversion |
|---|-----------|
| 1 | Celsius → Fahrenheit |
| 2 | Fahrenheit → Celsius |
| 3 | Celsius → Kelvin |
| 4 | Kelvin → Celsius |

---

##  Getting Started

### Prerequisites

- Python 3.13.6 installed on your system
- No external libraries required — uses only Python built-ins

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rajratna-D/UNIT-CONVERTER.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd UNIT-CONVERTER
   ```

3. **Run the program**
   ```bash
   python main.py
   ```

---

##  Usage

Once the program starts, you'll see the main menu:

```
UNIT CONVERTER
1: Length
2: Time
3: Temperature
0: Exit
Enter your choice:
```

Select a category, then choose a specific conversion, and enter your value. The result is displayed instantly.

**Example:**
```
Enter your choice: 3
1: Celsius to Fahrenheit
2: Fahrenheit to Celsius
3: Celsius to Kelvin
4: Kelvin to Celsius
Enter your choice: 1
Enter your value: 100
Celsius to Fahrenheit = 212.0 F
```

Enter `0` at the main menu to exit the program.

---

## Project Structure

```
UNIT-CONVERTER/
│
└── main.py        # Main application file containing all converter functions
```

---

## Contributing

Contributions are welcome! If you'd like to add more unit categories (e.g., Weight, Speed, Area) or improve the interface:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request



<p align="center">Made with love by <a href="https://github.com/Rajratna-D">Rajratna-D</a></p>
