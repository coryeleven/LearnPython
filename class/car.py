"""
    1.__init__是一个特殊的方法，每次调用函数都会执行
    2.创建car实例时，将自动传入实参的self，每个与类相关联的方法调用都自动传递实参self，是指向实例本身的一个引用
    3.以self为前缀的变量可供类中的所有方法调用
    4.继承
"""
"""一个可用于表示汽车的car"""
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

# super函数将父类与子类关联起来，给子类定义属性 battery_size
class ElectricCar(Car):
    def __init__(self,manufacturer, model, year):
        """
          初始化父类的属性，再初始化电动汽车特有的属性。
        """
        super().__init__(manufacturer, model, year)
        self.battery_size = 70
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This cat has a " + str(self.battery_size) + '-kWh battery!')
my_tesla = ElectricCar('tesla','mode s','2020')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
