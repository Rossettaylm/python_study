import matplotlib.pyplot as plt
from random_walk import RandWalk

# 创建一个RandWalk实例，并将其包含的点都表示出来
rw = RandWalk()
rw.fill_walk()

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, 
                cmap=plt.cm.Blues, s=15, edgecolor='none')

# 突出起点和终点
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], s=100, edgecolors='none', c='red')

# 隐藏坐标轴
plt.axis().get_xaxis().set_visible(False)
plt.axis().get_yaxis().set_visible(False)


plt.show()

