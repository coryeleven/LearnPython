# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 18:22
class Parent:
    def __init__(self):
        self.name = "Old Cory"
        self.age = 24
        self.gender ="man"
    def cook(self):
        print("do somting about luandun")
class Childen(Parent):
    def __init__(self):
        self.name = "Cory"
        self.age =100
    def cook(self):
        print("do somthing about shizitou")
        Parent.cook(self) #保留父类属性
c= Childen()
print(str(c.age) + "\t"  + str(c.name))
c.cook()


# class WhileError(Exception):
#     def __init__(self,err):
#         Exception.__init__(self,err)
# raise  WhileError("while is not found ")

#类型
class Jclass:
    pass
class Nclass(object):
    pass
print(type(Jclass))
print(type(Nclass))
print(type("a"))
print(dir(Jclass))
print(dir(Nclass))


class A:
    num = 10
class B(A):
    pass
class C(A):
    num = 100
class D(C,B):
    pass
A().num
B().num
C().num
D().num
d = D()
print(d.num)

class A:
    num = 10
class B(A):
    pass
class C(A):
    num = 100
class D(B,):
    pass
d = D()
print(d.num)

print("-----------多重继承-----------")
class A(object):
    a = 10
class B(A):
    b = 20

class C(A):
    a = 100
    c = 30
class D(B,C):
    pass
d = D()
print(d.a)
print(d.b)
print(d.c)

print("------------封装------------")
class Myclass:
    def __whiles(self):
        print("this is whiles ")
    def hello(self):
        self.__whiles()

m = Myclass()
m.hello()
# m.__whiles()

print("----------多态-- 同样的方法在不同的实例调用拥有不同的效果-------")
class A:
    pass
a = A()
#isinstance 判断指定实例是否是指定对象的实列
print(isinstance(a,A))


class Parent:
    def cook(self):
        print("do somthing about luandun")
class Children(Parent):
    def cook(self):
        print("do somthing about shizitou")
        Parent.cook(self) #调用父类的的方法
p = Parent()
c = Children()
print(isinstance(p,Parent))
print(isinstance(c,Parent))
p.cook()
c.cook()