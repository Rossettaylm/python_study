import matplotlib.pyplot as plt
from random_walk import RandWalk

rw = RandWalk(50000)
rw.fill_walk()

plt.figure(figsize=(10, 6), dpi=128)
plt.plot(rw.x_values, rw.y_values, linewidth=1, c='pink')
# plt.axis("off")
plt.show()
