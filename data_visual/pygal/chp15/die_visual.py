from die import Die
import pygal as pl

# 创建一个Die 6
die = Die()

# 掷100次骰子， 并将结果存储在一个列表中
results = []
for value in range(10000):
    result = die.roll()
    results.append(result)

# 分析结果, 遍历1～6,计算每面出现的频率
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 创建直方图，保存为svg文件
hist = pl.Bar()

hist.title = "Results of rolling one Die6 10000 times"
hist.x_labels = [1, 2, 3, 4, 5 ,6]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('Die6', frequencies)
hist.render_to_file('histogram_die6.svg')
