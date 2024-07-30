# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 00:50:25 2024

@author: marke
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep

# Example data
x_data = np.linspace(0, 10, 10)
y_data = np.sin(x_data)

# Create spline representation
spl = splrep(x_data, y_data)

# Evaluate spline
x_eval = np.linspace(0, 10, 100)
y_eval = splev(x_eval, spl)

# Plot data and spline interpolation
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_eval, y_eval, label='Spline interpolation', color='red')
plt.legend()
plt.show()
