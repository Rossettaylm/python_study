# self:实例的形参，make、model、year：实例的属性

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # python创建一个属性并赋予初始值

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) +
              " miles on it.")

    def update_odometer(self, meter):
        if meter >= self.odometer_reading:  # 防止回调里程表
            self.odometer_reading = meter
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


# 新建实例my_new_car
my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23  # 直接修改属性的值
my_new_car.read_odometer()

my_new_car.update_odometer(10)
my_new_car.update_odometer(27)  # 利用方法修改属性的值
my_new_car.read_odometer()

# 新建实例my_used_car
my_used_car = Car('subaru', 'outback', 2013)
print("\n")
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# 子类与父类


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
# super函数表示父类/superclass，即调用父类的__init__方法，使子类继承父类的属性
        self.battery = Battery()  # 添加一个实例作为属性

# 新建一个小类作为原类ElectricCar的一部分


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def get_range(self, car_model):
        self.car_model = car_model
        if self.car_model == 'model s':
            size = 240
        elif self.car_model == 'model l':
            size = 270
        message = "This car can go approximately " + str(size)
        message += " miles on a full charge."
        print(message)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print("\n" + my_tesla.get_descriptive_name())
#my_tesla.battery = Battery(85)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range('model s')
