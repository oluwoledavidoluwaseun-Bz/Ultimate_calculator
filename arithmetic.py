import math


def is_number(value):
    return isinstance(value, (int, float))


def add(num1, num2):
    if not is_number(num1) or not is_number(num2):
        return "Invalid input"
    return num1 + num2


def sub(num1, num2):
    if not is_number(num1) or not is_number(num2):
        return "Invalid input"
    return num1 - num2


def mul(num1, num2):
    if not is_number(num1) or not is_number(num2):
        return "Invalid input"
    return num1 * num2


def div(num1, num2):
    if not is_number(num1) or not is_number(num2):
        return "Invalid input"
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2


def floordiv(num1, num2):
    if not is_number(num1) or not is_number(num2):
        return "Invalid input"
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 // num2


def mod(num1, num2):
    if not is_number(num1) or not is_number(num2):
        return "Invalid input"
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 % num2


def exp(num):
    if not is_number(num):
        return "Invalid input"
    return math.exp(num)


def pow(base, exponent):
    if not is_number(base) or not is_number(exponent):
        return "Invalid input"
    return base ** exponent


def log(num, base=10):
    if not is_number(num) or not is_number(base):
        return "Invalid input"
    if num <= 0:
        return "Number must be greater than 0"
    if base <= 0 or base == 1:
        return "Invalid base"
    return math.log(num, base)



