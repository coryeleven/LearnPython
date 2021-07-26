# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 5:16 下午
# @File    : list_sort.py
# @Description :sort临时排序、永久排序

cars = ['bmw','audi','toyota','subaru']
print('list cras:',cars)

#sort 按照字母顺序排列,修改是永久性的
cars.sort()
print('list cars sort:',cars)

#reverse 与字母顺序相反，修改是永久性的
cars.sort(reverse=True)
print('list cars reverse:',cars)

cars = ['bmw','audi','toyota','subaru']
#sorted按照字母排序，只做临时修改
print("\nHere is the sorted list:",sorted(cars))
#sorted reverse临时倒序排列
print("Here is the sorted reverse list:",sorted(cars,reverse=True))
print('list cars:',cars)

cars.reverse() #reverse 反转列表排序，永久修改列表
print(cars)
print(len(cars)) #函数len 确定列表的长度

word = ['lundun','henan','beijing','guangzhou']
print(word)
print(sorted(word))
print(sorted(word,reverse=True))

print(word)
word.reverse()
print(word)
word.reverse()
print(word)
word.sort()
print(word)
word.sort(reverse=True)
print(word)
print(word)
print(len(word))
