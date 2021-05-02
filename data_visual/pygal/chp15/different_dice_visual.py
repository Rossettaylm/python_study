from die import Die
import pygal

# 创建一个Die6和Die10
die_1 = Die(6)
die_2 = Die(10)

results = []
for value in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Result of rolling a Die6 and Die10 50,000 times"
hist.x_labels = [num for num in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("Die6 + Die10", frequencies)
hist.render_to_file('histogram_diff_dice.svg')
