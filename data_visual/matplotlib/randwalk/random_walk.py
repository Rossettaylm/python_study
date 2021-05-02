from random import choice

class RandWalk():
    """一个生成随机漫步数据的类"""
    """一个存储漫步次数的变量，两个列表分别存储每次的横纵坐标"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有漫步都始于（0,0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            self.add_next_step(x_step, y_step)

        
    def get_step(self):
        # 决定前进方向以及沿着这个方向前进的距离
        direction = choice([1, -1])
        distance = choice(range(0,5))
        step = direction * distance
        return step


    def add_next_step(self, x_step, y_step):
        # 计算下一个点的x和y值
        next_x = self.x_values[-1] + x_step
        next_y = self.y_values[-1] + y_step
        self.x_values.append(next_x)
        self.y_values.append(next_y)

