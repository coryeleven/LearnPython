"""
    迭代是Python最强大的功能之一，是访问集合元素的一种方式。
    迭代器是一个可以记住遍历的位置的对象。
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
    迭代器有两个基本的方法：iter() 和 next()。
    字符串，列表或元组对象都可用于创建迭代器：
"""
#定义迭代器类，其是Mylist可迭代对象的迭代器类
class MylistIterator(object):
    def __init__(self,data):
        self.data = data
        self.now = 0  #当前迭代值，初始为 0 


    def __iter__(self):
        return self #返回该对象的迭代器类的实例，因为自己就是迭代器，所以返回self

    def __next__(self): #迭代器必须实现的方法
        while self.now < self.data:
            self.now += 1 
            return self.now - 1 
        raise StopIteration

my_list = MylistIterator(5)
print('使用for来遍历迭代器')
for i in my_list:
    print(i)

my_list = MylistIterator(10)
print('使用next来遍历迭代器')
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))

class Mylist(object):
    def __init__(self,num):
        self.data = num
    def __iter__(self):
        return MylistIterator(self.data)

my_list = Mylist(5)
print("使用for循环来遍历可迭代对象my_list")
for i in my_list:
    print(i)

my_list1 = Mylist(10)
print("使用next来遍历可迭代对象my_list")
#可迭代对象如果没有next方法，则无法通过next()进行遍历
print(next(my_list1))


