import pygal
from die import Die

# 创建两个骰子
die_1 = Die()
die_2 = Die()

results = []
for value in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist=pygal.Bar()
hist.title = "Results of rolling two Die6 1000 times."
hist.x_labels = [num for num in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('Die6+Die6', frequencies)
hist.render_to_file("histogram_dice.svg")


