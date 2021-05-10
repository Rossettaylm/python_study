###############################################################
# File Name: zip.py
# =============================================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-
##############################################################
import matplotlib.pyplot as plt

x = list(range(10))
y = [value ** 2 for value in x]

# zip()函数return 一个元组
zipped = zip(x, y)
for tp in zipped:
    print(tp)

coordinate = []
for i in range(10):
    coordinate.append((x[i], y[i]))

x2, y2 = zip(*coordinate)

plt.figure(dpi=128, figsize=(10, 6))
plt.plot(x2, y2, linewidth=6, c='pink')
plt.title("test zip", fontsize=16)

plt.xlabel("X", fontsize=14)
plt.ylabel("The square of X", fontsize=14)
plt.axis([0, 11, 0, 110])

plt.show()
