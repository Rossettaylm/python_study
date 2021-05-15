#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-10, 10)
y = np.exp(x)

plt.figure(figsize=(10, 6), dpi=128)
plt.plot(x, y, c='pink', linewidth=3)
plt.title("The power funtion of e")
plt.axis([-5, 10, 0, 10000])
plt.show()
