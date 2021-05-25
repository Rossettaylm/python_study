"""
AM_modulation from numpy
"""
import matplotlib.pyplot as plt
import numpy as np

pi = np.pi
Fs = 10000
Fc = 10
x = np.linspace(0, 8*pi, 8*Fs)
carrier = np.array([np.sin(2*pi*Fc*value) for value in x], dtype=float)
modulation = np.array([np.sin(2*pi*value) for value in x], dtype=float)
AM_modulation = carrier * modulation
plt.figure(figsize=(10, 6), dpi=128)
plt.plot(x, AM_modulation, c='pink', linewidth=3)
plt.axis([0, 2*pi, -2, 2])
plt.show()
