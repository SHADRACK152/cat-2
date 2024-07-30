# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 03:15:14 2024

@author: marke
"""

import numpy as np

def power_iteration(A, num_simulations: int):
    b = np.random.rand(A.shape[1])
    for _ in range(num_simulations):
        b = np.dot(A, b)
        b = b / np.linalg.norm(b)
    eigenvalue = np.dot(b.T, np.dot(A, b))
    return eigenvalue, b

def qr_algorithm(A, num_simulations: int):
    A_copy = np.copy(A)
    for _ in range(num_simulations):
        Q, R = np.linalg.qr(A_copy)
        A_copy = np.dot(R, Q)
    eigenvalues = np.diag(A_copy)
    return eigenvalues

# Matrix A
A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

# Perform power iteration
eigenvalue_power, eigenvector_power = power_iteration(A, 1000)
print("Power Iteration Eigenvalue:", eigenvalue_power)
print("Power Iteration Eigenvector:", eigenvector_power)

# Perform QR algorithm
eigenvalues_qr = qr_algorithm(A, 1000)
print("QR Algorithm Eigenvalues:", eigenvalues_qr)
