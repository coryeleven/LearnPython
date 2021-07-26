def mylist(num): #定义生成器
    now = 0 
    while now < num:
        val = (yield now) #返回当前迭代值
        now = now + 1 if val is None else val #val为none,迭代之自增1，否则重新开始

"""
    yeid可以理解为return,返会给后面的调用者，不同的是return 返回后，函数会释放，而生成器则不会
"""

my_list = mylist(10)
print("使用for循环来遍历可迭代对象my_list")
for i in my_list:
    print(i)


my_list1 = mylist(5)
print("使用next来遍历可迭代对象my_list")
print(next(my_list1))
print(next(my_list1))
print(next(my_list1))