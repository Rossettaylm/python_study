import matplotlib.pyplot as plt
from random_walk import RandWalk  # type: ignore

# 创建一个RandWalk实例，并将其包含的点都表示出来
rw = RandWalk(50000)
rw.fill_walk()

# 设置绘图窗口的尺寸, 单位为英寸
plt.figure(figsize=(10, 6), dpi=128)

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
            cmap=plt.cm.Blues, edgecolors='none', s=1)  # type: ignore

# 突出起点和终点
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], s=100, edgecolors='none', c='red')

plt.axis('off')


plt.show()

