# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 02:02:55 2024

@author: marke
"""

import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_rule(f, a, b, n):
    """
    Approximate the integral of f from a to b using the Trapezoidal Rule with n subintervals.
    
    :param f: Function to integrate
    :param a: Lower bound of the integral
    :param b: Upper bound of the integral
    :param n: Number of subintervals
    :return: Approximate integral value
    """
    # Compute the width of each subinterval
    h = (b - a) / n
    
    # Compute the x values where we evaluate the function
    x = np.linspace(a, b, n+1)
    
    # Compute the function values at these points
    y = f(x)
    
    # Apply the Trapezoidal Rule
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    
    return integral

# Define the function to integrate
def func(x):
    return np.sin(x)  # Example function: sin(x)

# Integration bounds
a = 0
b = np.pi

# Number of subintervals
n = 10

# Compute the integral using the Trapezoidal Rule
integral_value = trapezoidal_rule(func, a, b, n)
print(f"Approximate integral value: {integral_value:.4f}")

# Plotting the function and trapezoids
x = np.linspace(a, b, 1000)
y = func(x)

# Create trapezoid lines for visualization
x_trap = np.linspace(a, b, n+1)
y_trap = func(x_trap)
plt.plot(x, y, label='f(x) = sin(x)')
plt.fill_between(x_trap, 0, y_trap, alpha=0.3, color='orange', label='Trapezoids')

plt.title('Trapezoidal Rule Integration')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()



