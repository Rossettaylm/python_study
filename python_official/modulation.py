import numpy as np
import matplotlib.pyplot as plt

pi, sin = np.pi, np.sin
Fc, Fw, Ac = 10, 1, 2
Fs = 10000
x = np.linspace(0, 2 * pi, Fs)
carrier = np.array([sin(2 * pi * Fc * t) for t in x])
modulate = np.array([sin(2 * pi * Fw * t) for t in x])
AM = Ac * (1 + modulate) * carrier
print(AM.max())

plt.figure(figsize=(10, 6), dpi=128)
plt.plot(x, AM, c='pink', linewidth=2)
plt.title('AM_modulation', fontsize=16)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.axis([0, 2 * pi, -5, 5])
plt.show()
