# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 01:45:08 2024

@author: marke
"""

import numpy as np
import matplotlib.pyplot as plt

def compute_fft(signal, sample_rate):
    """
    Computes the FFT of a signal and returns the frequency and magnitude.
    """
    n = len(signal)
    # Compute the FFT
    fft_signal = np.fft.fft(signal)
    # Compute the magnitude
    magnitude = np.abs(fft_signal) / n
    # Compute the frequency bins
    frequencies = np.fft.fftfreq(n, d=1/sample_rate)
    # Only keep the positive frequencies
    mask = frequencies >= 0
    return frequencies[mask], magnitude[mask]

def generate_signal(f1, f2, sample_rate, duration):
    """
    Generates a signal composed of two sinusoidal components.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    return t, signal

# Parameters
f1 = 50
f2 = 120
sample_rate = 1000
duration = 1

# Generate the signal
t, signal = generate_signal(f1, f2, sample_rate, duration)

# Compute the FFT
frequencies, magnitude = compute_fft(signal, sample_rate)

# Plot the signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Time Domain Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Plot the FFT
plt.subplot(2, 1, 2)
plt.plot(frequencies, magnitude)
plt.title('Frequency Domain Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.tight_layout()
plt.show()














