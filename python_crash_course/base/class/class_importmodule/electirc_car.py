# 从一个模块中导入另一个模块
from car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            carrange = 240
        elif self.battery_size == 85:
            carrange = 270
        message = "This car can go approximately " + str(carrange)
        message += " miles on a full charge."
        print(message)
