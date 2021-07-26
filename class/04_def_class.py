# -*- coding: utf-8 -*-

class Bird:
    def __init__(self):
        print("this is instance method")

    def func():
        print("this is a function")
    @classmethod
    def cMethod(cls):
        Bird.age = 5
        cls.age = 10
        print("this is a class method")

    @staticmethod
    def sMethod():
        print("this is a static method")
b = Bird()
b.cMethod()
Bird.cMethod()
print(Bird.age)

print("\n装饰器")
def doLogo(fun):
    def Logo():
        print("this is cory's logo")
        fun()
    return  Logo
@doLogo
def jp():
    print("jp")
@doLogo # 相当于调用了doLogo(fun)
def sb():
    print("sb")
jp()
sb()

print("-----------构造函数特点-----------")
#1.构造函数在类实例化之后自动执行
class Bird:
    def __init__(self):
        print("I am a bird,I am so happy")
b = Bird()

#2 构造函数在实例化时传参,在实例化得时候传递参数
class Bird:
    def __init__(self,name):
        print("I am a bird,my name is %s I am so happy" %name)
b = Bird("cory")

#3 构造函数不能有返回值
class Bird:
    def __init__(self):
        print("I am a bird,I am so happy")
        return 1
# b = Bird()


print("------------------")
class Example:
    def __init__(self):
        self.name = "Example"
    def cook(self):
        print("I can cook")

e = Example()
print(hasattr(e,"cook"))
print(hasattr(Example,"cook"))

setattr(e,"age",24)
setattr(Example,"age",25)
print(e.age)
print(Example.age)

def nice(self):
    print("so nice")
# setattr(Example,"age",nice)
setattr(e,"age",nice())
print(Example.name)
print(e.age)

delattr(e,"name")
print(e.name)
e.age = 100
print(e.age)