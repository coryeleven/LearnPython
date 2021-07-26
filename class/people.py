# -*- coding: utf-8 -*-
class People:
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name= n
        self.age= a #定义私有属性,私有属性在类外部无法直接进行访问
        self._weight= w
        print('这是父类')
 
    def speak(self):
        print('%s 说,我今年%d岁了，体重%s 斤' % (self.name,self.age,self._weight))

# 单继承类
class Student(People):
    def __init__(self, n, a, w):
        # 调用方式一：调用父类的初始化方法，继承People类（最常用）
        # super()是指向继承列表的下一个
        # super().__init__(n, a, w)
        # print("调用student初始化方式一")
        # 调用方式二：调用父类的初始化方法
        People.__init__(self, n, a, w)
        print("调用People父类方式二")
    def speak(self):
        print('覆盖父类')
People('cory', 24, '80').speak()
Student('夏明', 25, '100').speak()


# 普通类
class Simple:
    def __init__(self, h, s):
        self.hobay= h
        self.sex= s
        print('我只是一个简单的类')
 
# 多继承
class School(Student, Simple):
    def __init__(self, n, a, w, h, s):
        Student.__init__(self, n, a, w)
        Simple.__init__(self, h, s)
        print('我是Student和Simple的儿子')
 
    def print_school(self):
        self.speak()
 
# 单继承调用
print(Student.mro())  # [<class '__main__.Student'>, <class '__main__.People'>, <class 'object'>]
stu = Student('wx', 18, 50)

# 多继承调用
sch= School('wx',18,50,'job','boy')
sch.speak()