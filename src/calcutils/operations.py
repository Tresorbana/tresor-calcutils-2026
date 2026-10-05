"""
operations.py
Core arithmetic and statistical helper functions for calcutils.
"""

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Returns the quotient of two numbers. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def mod(a: float, b: float) -> float:
    """Returns the remainder of the division of two numbers. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot perform modulo with zero divisor")
    return a % b

def average(numbers: list) -> float:
    """Returns the arithmetic mean of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)