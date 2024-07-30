# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 00:26:48 2024

@author: marke
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Example data
x_data = np.linspace(0, 4, 50)
y_data = x_data**2 + np.random.normal(0, 1, 50)

# Define a model function
def model_func(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the model to the data
params, params_covariance = curve_fit(model_func, x_data, y_data)

# Plot data and fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, model_func(x_data, *params), label='Fitted curve', color='red')
plt.legend()
plt.show()
