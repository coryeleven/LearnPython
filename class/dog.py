class Dog():
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting")
    def roll_over(self):
        print(self.name.title() + " is rolled over!")
mydog = Dog("旺财",6) #创建一个实列
print("My dog's name is " + mydog.name.title() + ".")
mydog.sit()
mydog.roll_over()

#9-1
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name.title() #定义变量
        self.cuisine_type = cuisine_type

    def  describe_restaurant(self):
        msg = self.restaurant_name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""
        msg = self.restaurant_name + " is open. Come on in!"
        print("\n" + msg)
restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2 三家餐馆
mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()

#9-3 用户

class User():
    def __init__(self,first_name,last_name,username,email,location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
    def describe_user(self):
        """显示用户信息摘要。"""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)
    def greet_user(self):
        """它向用户发出个性化的问候。"""
        print("\nWelcome back, " + self.username + "!")
eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()

#9-4就餐人数
print("\n9-4就餐人数")
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name.title() #定义变量
        self.cuisine_type = cuisine_type
        self.number_served = 0 #给属性指定默认值

    def  describe_restaurant(self):
        msg = self.restaurant_name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""
        msg = self.restaurant_name + " is open. Come on in!"
        print("\n" + msg)
    def set_number_served(self,number_served):
        """让用户能够设置就餐人数。"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """让用户能够增加就餐人数。"""
        self.number_served += additional_served

restaurant = Restaurant('the mean queen', 'pizza')
print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430 #修改属性的值
print("Number served: " + str(restaurant.number_served))

#设置就餐人数
restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))

#9-5尝试登录次数
print("\n尝试登录次数")
class User():
    def __init__(self,first_name,last_name,username,email,location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0
    def describe_user(self):
        """显示用户信息摘要。"""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)
    def greet_user(self):
        """它向用户发出个性化的问候。"""
        print("\nWelcome back, " + self.username + "!")
    def increment_login_attempts(self):
        """将login_attempts +1 """
        self.login_attempts += 1
    def reset_login_attempts(self):
        """将login_attempts重置为0。"""
        self.login_attempts = 0
eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print("\tLogin attempts: " + str(eric.login_attempts))

print("Resetting login attempts...")
eric.reset_login_attempts()
print("\tLogin attempts test: " + str(eric.login_attempts))





