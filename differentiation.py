# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 00:22:07 2024

@author: marke
"""
import numpy as np

def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Example function
f = lambda x: x**2

# Point at which to differentiate
x = 2

# Compute the derivative
derivative = numerical_derivative(f, x)
print(f"Numerical Derivative at x={x}: {derivative}")






import numpy as np

def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Example function
f = lambda x: x**2

# Point at which to differentiate
x = 2

# Compute the derivative
derivative = numerical_derivative(f, x)
print(f"Numerical Derivative at x={x}: {derivative}")

