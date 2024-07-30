# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 00:25:16 2024

@author: marke
"""

import scipy.integrate as spi

# Example function
f = lambda x: x**2

# Integrate f from 0 to 1
integral, error = spi.quad(f, 0, 1)
print(f"Numerical Integration: {integral}")
