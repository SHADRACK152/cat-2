# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 01:25:37 2024

@author: marke
"""
def f(x):
    return x**3 - 0.165*x**2 + 3.993e-4

def f_prime(x):
    return 3*x**2 - 0.33*x

def newtons_method(x0, iterations, tol=1e-5):
    x = x0
    for i in range(iterations):
        x_new = x - f(x)/f_prime(x)
        abs_relative_error = abs((x_new - x) / x_new) * 100
        print(f"Iteration {i+1}: x = {x_new}, f(x) = {f(x_new)}, Absolute Relative Approximate Error = {abs_relative_error}%")
        x = x_new
        if abs_relative_error < tol:
            break
    return x

# Initial guess
x0 = 0.03

# Number of iterations
iterations = 3

# Perform Newton's method
root = newtons_method(x0, iterations)
print(f"Estimated root after {iterations} iterations: {root}")
