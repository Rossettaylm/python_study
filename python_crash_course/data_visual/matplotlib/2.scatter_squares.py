import matplotlib.pyplot as plt

# 绘制散点图,s = size表示尺寸, c = color 表示颜色, cmap = colormap表示颜色映射
x_values = list(range(1, 1001))
y_values = [value ** 2 for value in x_values]
# 1.关键字表示颜色
# plt.scatter(x_values, y_values, c='red', s=40, edgecolors='none')

# 2.RGB表示颜色，取0~1
# plt.scatter(x_values, y_values, edgecolors='none', c=(0.4, 0.5, 0.5), s=20)

# 3.将c设置成y值列表，并使用参数cmap告诉pyplot使用蓝色映射
plt.scatter(x_values,
            y_values,
            c=y_values,
            cmap='Blues',
            edgecolors='none',
            s=40)

# 设置散点图标题并给坐标轴加上标签
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
# 保存文件，依次为文件名， 裁剪类型为tight
# plt.savefig('squares_plot.png', bbox_inches='tight')
