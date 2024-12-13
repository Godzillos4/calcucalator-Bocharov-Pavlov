import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    return a / b

def modulus(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    return round(a % b, 10)

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Квадратный корень из отрицательного числа невозможен.")
    return math.sqrt(a)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def floor(a):
    return math.floor(a)

def ceil(a):
    return math.ceil(a)
