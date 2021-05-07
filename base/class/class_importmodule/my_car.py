from car import Car  # type: ignore
from car import ElectricCar  # type: ignore 从car.py引进ElectricCar类，其分类Battery不用
#from car import Car,ElectricCar
# import car     #导入整个模块需要加前缀，如car.Car()

my_new_car = Car('audi', 'a4', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print("\n")
my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.odometer_reading = 100
my_tesla.update_odometer(2333)
my_tesla.read_odometer()
my_tesla.battery.battery_size = 85
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n")
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_beetle.odometer_reading = 3000
my_beetle.read_odometer()
my_beetle.increment_odometer(333)
my_beetle.read_odometer()
