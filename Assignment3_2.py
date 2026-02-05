"""
Docstring for Assignment3_2

Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
"""

import math as mt

num = int(input("Enter the number: "))

sq_root = mt.sqrt(num)
log_b = mt.log(num)
sine = mt.sin(num)
print(f"Square root of {num} is {sq_root}")
print(f"Logarithm of {num} is {log_b}")
print(f"Sine of {num} is {sine}")
