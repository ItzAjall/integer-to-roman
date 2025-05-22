# Integer to Roman Numerals Converter

This Python script provides a function to convert an integer into its Roman numeral representation.

## 🔍 Overview

The script includes a single function `Inttoroman(num: int)` that takes an integer input and returns its Roman numeral equivalent as a string.

### Example
```python
print(Inttoroman(900))  # Output: CM
```

## 📌 Features

- Converts integers to Roman numerals following the standard rules.
- Handles all typical Roman numeral ranges (1 to 3999).
- Custom logic for subtractive notation (e.g., IV, IX, XL, etc.).

## 🚀 How It Works

1. The function breaks the number into its place value components (units, tens, hundreds, thousands).
2. It maps each component to the corresponding Roman numeral using a custom logic and dictionary of symbols.
3. It handles special subtractive cases like 4, 9, 40, 90, etc., appropriately.

## 🛠️ Requirements

- Python 3.x

No external libraries are required.

## 📂 File Structure

```
├── integer-to-roman.py  # Contains the Inttoroman function
└── README.md           # This file
```

## 📌 Usage

Simply import or call the `Inttoroman` function in your Python script:

```python
from integer-to-roman import Inttoroman

print(Inttoroman(1987))  # Output: MCMLXXXVII
```
