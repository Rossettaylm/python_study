import matplotlib.pyplot as plt


input_value = list(range(1, 6))
squares = [1, 4, 9, 16, 25]
plt.plot(input_value, squares, linewidth=5, c='pink')

# 设置图标标题，并给坐标轴加上标签
plt.title("Squares Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
