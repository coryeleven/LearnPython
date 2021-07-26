# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 4:48 下午
# @File    : tuple_operation.py
# @Description :

#元组 python 将不可能修改的列表称为元组,使用（）定义
deimension = (100,20)
print(deimension[0])
# deimension[0]=200
print(deimension)
#遍历元组中所有的值
for i in deimension:
    print(i)
deimension = (123,456)
for i in deimension:
    print(i)

restaurant = ('米饭','面食','粥','黄焖鸡','煲仔饭')
print(restaurant)
for i in restaurant:
    print(i)
#restaurant[0] = '盖浇饭'
restaurant = ('米饭','面食','粥','酸菜鱼','烤肉拌饭')
print(restaurant)
for i in restaurant:
    print(i)