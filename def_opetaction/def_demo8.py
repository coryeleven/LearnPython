# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 9:22

def say_hello(name,age):
    print("Hello %s,he is %s years old"%(name,age))

say_hello("cory",24)
say_hello(24,"cory")

#通过给形参前面添加*,使参数变成 一个元组 ，所有传递的参数变成元组的元素
def say_hello1(*args):
    print(args)
say_hello1()
say_hello1('1')
say_hello1(1,2,3,4,5)

#通过给形参前面添加使参数变成一个字典,所有传递的参数变成字典的键值对
def say_hello2(**args):
    print(args)
say_hello2()
say_hello2(a = 1)
say_hello2(a = 1,b = 2,c = 3,d = 4,e = 5)

#Lambda匿名函数 ,def函数是语句块，lambda函数是表达式，def函数拥有函数名，lambda函数没有
A = lambda a:a+1
print(A(2))

# def hello(a,b):
#     return  a+b
# print(hello(2,2))
#
# print(map(hello,range(1,6),range(6,11)))

print("装饰器")
def  say_sayhello():
    print("Hello World!")

print(say_sayhello) #函数本身
print(say_sayhello()) #调用的是函数的功能

#闭包 在函数内部对嵌套层进行return 或者其他操做
print ('\nhi')
def hello():
    def hi():
        print(123)
    return hi #返回函数hi 本身
# print(hello()())
hello()() #调用函数的功能

print("\n--------------------")
def outer():
    def inner():
        print("this is inner")
    return  inner
print(outer())
outer()()



print("\n---------嵌套传参-----------")
def outer(name):
    def inner(age):
        print("%s is %s years old"%(name,age))
    return inner
outer('Cory')('18')



print("\n------给函数加括号是为了调用函数--------")
def outer(fun):
   # print("我是函数outer")
    print("我是return返回的")
    def inner():
        print("Hello,I'm Cory")
        fun()  #fun == age fun()==age()
    return inner
def age():
    print("I'm 24 years old")

outer(hello) #实参
outer(age)() #

# print(age)  #age 返回函数age 本身
# print(age()()) #调用的函数的功能


print('\n-----装饰器-----')

def say(fun):
    print("我是return返回的")
    def say_hello():
        print("Hello,I'm Cory")
        fun()
    return say_hello
@say # test == say(test)
def test():
    print("I'm 24 years old")
# say(test)()
test()