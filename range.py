# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 4:40 下午
# @File    : range.py
# @Description :
# range() 指定步长，函数从2开始，每次加3，直至达到或不超过终值

#rang生成一个列表
even_numbers = list(range(2,20,3))
print(even_numbers)

# ** 乘方运算
squares = []
for values in range(1,11):
    square = values**2
    squares.append(square) #append 追加之列表元素的末尾
print(squares)
print(max(squares))
print(min(squares))
print(sum(squares))

#列表解析将for循环和创建新元素的代码合并成一行
square1 = [i**2 for i in range(1,5)]
print(square1)


# 指定步长，函数从3开始，每次加N
for i in range(1,20,2):
    print(i)
print(list(range(3,30,2)))
print(list(range(3,30,3)))
print(list(range(3,30,4)))

numbers = [i**3 for i in range(1,11)]
print(numbers)

