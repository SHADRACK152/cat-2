# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 00:43:05 2024

@author: marke
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Example data
x_data = np.linspace(0, 10, 100).reshape(-1, 1)
y_data = 2 * x_data + 1 + np.random.normal(0, 1, 100).reshape(-1, 1)

# Create and fit the model
model = LinearRegression()
model.fit(x_data, y_data)

# Predict
y_pred = model.predict(x_data)

# Plot data and regression line
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, y_pred, label='Regression line', color='red')
plt.legend()
plt.show()

print(f"Coefficient: {model.coef_}")
print(f"Intercept: {model.intercept_}")
