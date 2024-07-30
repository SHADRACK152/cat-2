# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 02:15:43 2024

@author: marke
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the data points
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([5.5, 43.1, 128, 290.7, 498.4, 979.67])

# Fit a 3rd-degree polynomial to the data
degree = 3
p = np.polyfit(x, y, degree)

# Define the range for plotting the polynomial
x2 = np.arange(1, 6.1, 0.1)
y2 = np.polyval(p, x2)

# Plot the data points and the polynomial fit
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Data Points')
plt.plot(x2, y2, '-', label=f'Polynomial Fit (Degree {degree})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Fit Using the Trapezoidal Rule')
plt.legend()
plt.grid(True)
plt.show()
