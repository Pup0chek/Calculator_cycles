import math



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def remainder(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))