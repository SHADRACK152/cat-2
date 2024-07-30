# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 00:52:36 2024

@author: marke
"""

import numpy as np

# Given data points
x_points = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y_points = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# Target x value for interpolation
x_target = 4.0

# Points for linear interpolation
x1, y1 = x_points[0], y_points[0]
x2, y2 = x_points[1], y_points[1]

# Linear interpolation formula
y_target = y1 + (y2 - y1) / (x2 - x1) * (x_target - x1)
y_target

