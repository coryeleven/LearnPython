# -*- coding: utf-8 -*-
from car import Car
class Battery():
    """一次模拟电动汽车电瓶的简单测试"""
    def __init__(self,battery_size=85):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
class ElectricCar(Car):
    """电动车的独特之处"""
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

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

my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla)
my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


