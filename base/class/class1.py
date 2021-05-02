# 一般类的命名规则为首字母大写
# self表示实例的形参
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")
    
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 定义的sit和roll_over是类中的方法
my_dog.sit()
my_dog.roll_over()
