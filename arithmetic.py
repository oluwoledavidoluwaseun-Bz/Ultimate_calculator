# modules/arithmetic.py

import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def floordiv(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a // b


def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a % b


def exp(a, b):
    return a ** b


def power(a, b):
    return math.pow(a, b)


def log(a, b):
    if a <= 0:
        raise ValueError("Logarithm value must be greater than zero.")

    if b <= 0 or b == 1:
        raise ValueError("Logarithm base must be greater than zero and not equal to one.")

    return math.log(a, b)