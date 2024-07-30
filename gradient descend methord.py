# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 03:28:13 2024

@author: marke
"""

import numpy as np

def gradient_descent(learning_rate, initial_guess, num_iterations):
    # Define the function and its gradient
    def f(x, y):
        return x**2 + y**2 - x*y + x - y + 1
    
    def gradient(x, y):
        df_dx = 2*x - y + 1
        df_dy = 2*y - x - 1
        return np.array([df_dx, df_dy])
    
    # Initialize the starting point
    x, y = initial_guess
    
    # Perform gradient descent
    for _ in range(num_iterations):
        grad = gradient(x, y)
        x -= learning_rate * grad[0]
        y -= learning_rate * grad[1]
    
    return x, y, f(x, y)

# Parameters
learning_rate = 0.1
initial_guess = (0, 0)
num_iterations = 100

# Perform gradient descent
min_x, min_y, min_f = gradient_descent(learning_rate, initial_guess, num_iterations)

print("Minimum x:", min_x)
print("Minimum y:", min_y)
print("Function value at minimum:", min_f)
