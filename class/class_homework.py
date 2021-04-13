class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("\nThe restaurant name is " + self.restaurant_name.title()
                + ".")
        print("The cuisine type of this restaurant is " +
                str(self.cuisine_type))
    def open_restaurant(self):
        print("\n" + self.restaurant_name.title() + " is openning!")
    
restaurant1 = Restaurant('waipo laofan', 10)
restaurant2 = Restaurant('zhou mapo', 12)
restaurant3 = Restaurant('tianfu yuzhuang', 15)
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant1.open_restaurant()

# 父类
class User():
    def __init__(self, first_name, last_name, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.full_name = self.first_name + ' ' + self.last_name
    def describe(self):
        print("\nYour name: " + self.full_name.title())
        print("Your address: " + self.location.title())
        print("Your age: " + str(self.age))
    def greet_user(self):
        print("Hello! " + self.full_name.title())

user = User(first_name = 'yang',last_name = 'liaoming',
        location = 'jiangle',age = 21)
user.describe()
user.greet_user()

# 子类
class Admin(User):
    def __init__(self, first_name, last_name, location, age):
        super().__init__(first_name, last_name, location, age)
        self.prv = Privileges() # Privileges中的属性必须有默认值


# 子类中的分类
class Privileges():
    def __init__(self, privileges = ['default']):   #privileges必须有默认值
        self.privileges = privileges
    def show_privileges(self):
        print("\nHello! Your privileges include: ")
        for privilege in self.privileges:
            print(privilege)

root = Admin('yang', 'liaoming', "xi'an", 21)
#root.prv.privileges = ['can add post', 'can delete post', 'can ban user']
root.prv.show_privileges()
