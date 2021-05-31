import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期，最高气温, 最低气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # 阅读器对象返回下一行，即第一行
    header_row = next(reader)

    # enumerate()来获取header_row每个元素的索引和其值
    # for index, column_header in enumerate(header_row):
    #print(index, column_header)

    dates, highs, lows = [], [], []
    # 阅读器对象将从第二行开始遍历
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

# 填充最高温和最低温之间的区域，alpha表示透明度
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA",
          fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)

# 绘制斜的日期标签, 防止重叠
fig.autofmt_xdate()

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
