#9-6冰淇淋小店

class Restaurant():
    """一个表示餐馆的类。"""
    def __init__(self, name, cuisine_type):
        """初始化餐馆。"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """显示餐馆信息摘要。"""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """让用户能够设置就餐人数。"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """让用户能够增加就餐人数。"""
        self.number_served += additional_served
#继续父类
class IceCreamStand(Restaurant):
    #初始化父类的属性，增加新的flavor 属性
    def __init__(self,name,cuisine_type='ice_ream'):
        #super() 关联父类和子类的函数
        super().__init__(name,cuisine_type)
        #给子类添加新的属性
        self.flavors = []
    def show_flavors(self):
        """显示冰激淋的品种"""
        print("\nWe hava the following flavors available:")
        for flavor in self.flavors:
            print("- " +  flavor.title())
big_one = IceCreamStand("The big one")
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']
big_one.describe_restaurant()
big_one.show_flavors()


#9-7管理员

print("\n9-7")
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
        """它向用户发出个性化的问候"""
        print("\nWelcome back, " + self.username + "!")
class Admin(User):
    def __init__(self,first_name,last_name,username,email,location):
        super().__init__(first_name,last_name,username,email,location)
        self.privuleges = []
    def show_privuleges(self):
        for privalehes in self.privuleges:
            #它向用户发出个性化的问候
            print("\t -" + privalehes )
#创建一个实列
eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
#实列调用父类User() 中的方法
eric.describe_user()

eric.privuleges=[
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
eric.show_privuleges()

#9-8权限
class Admin(User):
    """有管理权限的用户。"""
    def __init__(self, first_name, last_name, username, email, location):
        """初始化管理员。"""
        super().__init__(first_name, last_name, username, email, location)
        # 将权限集初始化为空。添加self.provilieges属性，其实是调用Privileges 类
        self.privileges = Privileges()
class Privileges():
    def __init__(self,privileges=[]):
        #Privileges类初始化一个属性
        self.privileges = privileges
    def show_privileges(self):
        #显示其权限
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("\t" + privilege)
        else:
            print("- This user has no privileges.")
eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()
print("\nAdding privileges...")
#通过父类的属性调用子类中的属性privileges，创建实例 赋值
eric.privileges.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
#父类实例 查找属性 privileges，并创建Privileges实列调用show_privileges
eric.privileges.show_privileges()

#9-9电瓶升级
class Car():
    def __init__(self,manufacturer, model, year):
        #初始化汽车属性
        self.manufacturer = manufacturer
        self.model = model
        self.year =year
        #添加一个历程的属性，默认值为0
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回汽车的描述信息"""
        long_name = str(self.year) + " " + self.manufacturer + " " + self.model
        return  long_name.title()
    def read_odometer(self):
        """打印汽车的里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mileage):
        """可以修改里程表"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        self.odometer_reading += miles

class Battery():
    """一次模拟电动汽车电瓶的简单测试"""
    def __init__(self,battery_size=60):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            message = "This car can go approximately " + str(range)
            message += " miles on a full charge."
            print(message)

    def upgrade_battery(self):
            """在可能的情况下将电瓶升级。"""
            if self.battery_size == 60:
                self.battery_size = 85
                print("Upgraded the battery to 85 kWh.")
            else:
                print("The battery is already upgraded.")
class ElectricCar(Car):
    def __init__(self,manufacturer, model, year):
        """
               初始化父类的属性，再初始化电动汽车特有的属性。
               """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

