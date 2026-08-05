import numpy as np

def evaluate_polynomial(coefficients, x):
    return sum(coefficients[i]*(x**i) for i in range(len(coefficients)))

def finite_difference_derivative(coefficients, x, h):
    """
    Returns: the polynomial value at x, the value at x plus h, and the forward-difference slope
    """
    base_val = evaluate_polynomial(coefficients, x)
    shifted_val = evaluate_polynomial(coefficients, x + h)
    discrete_derivative = (shifted_val - base_val) / h
    return (base_val, shifted_val, discrete_derivative)