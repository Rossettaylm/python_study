"""
AM_modulation from numpy
"""
import matplotlib.pyplot as plt
import numpy as np

pi = np.pi
Fs = 10000
Fca = 10
Fcf = 5
x = np.linspace(0, 8 * pi, 8 * Fs)
carrier = np.array([np.sin(2 * pi * Fca * value) for value in x], dtype=float)
modulation = np.array([np.sin(2 * pi * value) for value in x], dtype=float)
AM_modulation = carrier * modulation
FM_modulation = [np.cos(2 * pi * Fcf * t + 2 * np.cos(2 * pi * t)) for t in x]

plt.figure(1, figsize=(10, 6), dpi=128)

plt.subplot(2, 1, 1)
plt.plot(x, AM_modulation, c='pink', linewidth=2)
plt.legend('AM')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.axis([0, 2 * pi, -2, 2])

plt.subplot(2, 1, 2)
plt.plot(x, FM_modulation, c='blue', linewidth=2)
plt.legend('FM')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.axis([0, 2 * pi, -2, 2])

plt.savefig('modulation.png')
