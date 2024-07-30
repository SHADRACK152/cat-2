# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 02:51:16 2024

@author: marke
"""

import numpy as np
import matplotlib.pyplot as plt

# Function to compute Lagrange polynomial coefficients
def lagrange_coefficients(x, y):
    def lagrange_basis(x, xi, xj):
        """Compute the Lagrange basis polynomial L_i(x)."""
        term = 1
        for xj_val in xj:
            if xj_val != xi:
                term *= (x - xj_val) / (xi - xj_val)
        return term

    def lagrange_polynomial(x, x_data, y_data):
        """Compute the Lagrange polynomial."""
        n = len(x_data)
        L = np.zeros_like(x)
        for i in range(n):
            xi = x_data[i]
            yi = y_data[i]
            L += yi * lagrange_basis(x, xi, x_data)
        return L

    # Create a fine grid to evaluate the polynomial
    x_grid = np.linspace(min(x), max(x), 500)
    y_poly = lagrange_polynomial(x_grid, x, y)
    
    # Fit a polynomial to the evaluated Lagrange polynomial
    coeff = np.polyfit(x_grid, y_poly, len(x) - 1)
    return coeff

# Function to compute Newton's divided difference polynomial coefficients
def newton_divided_difference(x, y):
    n = len(x)
    coeff = np.zeros(n)
    coeff[0] = y[0]

    # Compute divided differences
    for i in range(1, n):
        coeff[i] = (y[i] - np.polyval(np.poly1d(coeff[:i]), x[i])) / np.prod(x[i] - x[:i])

    return coeff

def newton_polynomial(x, coeff, x_data):
    """Evaluate the Newton polynomial at points x."""
    n = len(coeff)
    result = np.zeros_like(x)
    for i in range(n):
        term = coeff[i]
        for j in range(i):
            term *= (x - x_data[j])
        result += term
    return result

# Given data points
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

# Lagrange interpolation
coeff_lagrange = lagrange_coefficients(x, y)
x_grid = np.linspace(min(x), max(x), 500)
y_lagrange = np.polyval(np.poly1d(coeff_lagrange), x_grid)

# Newton's divided difference interpolation
coeff_newton = newton_divided_difference(x, y)
y_newton = newton_polynomial(x_grid, coeff_newton, x)

# Plotting the results
plt.figure(figsize=(12, 6))
plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_grid, y_lagrange, label='Lagrange Polynomial', linestyle='--')
plt.plot(x_grid, y_newton, label='Newton Polynomial', linestyle='-.')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Lagrange and Newton Interpolating Polynomials')
plt.legend()
plt.grid(True)
plt.show()

