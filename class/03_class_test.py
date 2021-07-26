# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 15:24
# @Author  : 海绵宝宝cory！！
# @FileName: 03_class_test.py
# @Software: PyCharm

class Bird:
    hungry = 100
    def eat(self):
        print("ahh")
b = Bird() #实例化，方便以后调用
print(b.hungry)
b.eat()
print("++++++++++++++类的实例与类的本身++++++++++++++++")
print(Bird) #类的本身
print(Bird()) # 类的实例
print(Bird().hungry)
print(Bird().eat())

print("+++++++c鸟++++")
class Bird:
    hungry = 200
    def eat(self): #self 是 class 类的实例
        print(self)
c = Bird()
#实例和实例调用的方法的self 是同一个东西，也就是说self 是 class 类当中的实例
print(c)
c.eat() #当我们用实例调用实例的方法
Bird.eat(b) #类调用方法，并把实例传入


print("============全局变量=============")
class BirdA:
    hungry = 100
    def sing(self):
        self.hungry += 10
    def eat(self):
        self.hungry -= 10
b = BirdA()
print(b.hungry)
b.sing()
print(b.hungry)
print(BirdA.hungry)

c = BirdA()
print(BirdA.hungry)
c.eat()
c.eat()
print(c.hungry)
print(BirdA.hungry)

print("=============小鸟吃虫子=============")

class Bird_B:
    hungry = 50
    def sing(self):
        if self.hungry != 100 and self != 0:
           self.hungry += 10
           self.go_die()
        else:
            print("bird is die,please go out")
    def eat(self,foold):
        if self.hungry != 100 and self != 0:
            if foold == 'bug':
                self.hungry -= 10
            elif foold == 'bread':
                self.hungry -= 15
                print(self.hungry)
            elif foold == 'yao':
                self.hungry = 100
            self.go_die()
        else:
            print("bird is die,please go out")
    def go_die(self):
        if self.hungry >= 100:
            self.hungry = 100
            print("go die")
        elif self.hungry <= 0:
            self.hungry = 0
            print("go die")
        else:
            print("hungry\t" + str(self.hungry))


cs = Bird_B()
print(cs.hungry)
cs.eat('yao')
cs.eat('ya')

