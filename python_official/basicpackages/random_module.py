import math
import random

print(math.cos(math.pi / 4))
print(math.log(1024, 2))


# (0) random()函数返回一个0.0 <= N < 1.0 的浮点数
print(random.random())
#  (1) 整数用随机数
# 整数随机数生成,randrange(start, stop[, step])
# 相当于random.choice(range(0, 10))
print(random.randrange(0, 10))

# randint返回值满足a<=N<=b. 等于randrange(a, b+1)
print(random.randint(0, 10))
print(random.randrange(0, 10+1))


# (2) 序列用函数, seq=sequence
# choice(seq),从非空序列中返回一个随机元素
print(random.choice(range(10)))
print(random.choice([1, -1, 2, -2]))

# choices(population, weight=None, cumweight=None, k=1)
# weight: 权重 cumweight：累积权重, 计算程序将权重转为累积权重算
# weight=[10, 5, 30, 5] cum_weight=[10, 15, 45, 50]
# default: k=1, 返回的个数
print(random.choices([1, 2, 3], cum_weights=[10, 30, 55], k=2))

# 从1-1000的范围内随机收取100个数
print(random.sample(range(1000), k=100))
