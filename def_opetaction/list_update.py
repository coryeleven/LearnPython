# -*- coding: utf-8 -*-
# @Time    : 2021/7/25 3:24 下午
# @File    : list_update.py
# @Description :在函数中修改列表

print("模拟打印每个设计，知道没有未打印的设计为止")
def print_models(unprinted_models,complete_models):
    """
    模拟打印每个设计，知道没有未打印的设计为止
    打印每个设计后,都将其移动至列表complete_models中
    """
    while unprinted_models:
        current_models = unprinted_models.pop()
        #模拟打印过程
        print("Printing model :" + current_models.title())
        complete_models.append(current_models)
unprinted_models = ['iphone','huawei','xiaomi']
complete_models = []
print_models(unprinted_models,complete_models)
print(unprinted_models[:],complete_models)
print(complete_models)

def show_complete(complete_models):
    # 显示打印好的所有模型
    print("\nThe following models have been printed!")
    for complete_model in complete_models:
        print(complete_model)
show_complete(complete_models)


# 禁止函数修改列表
#8-9
print("\n.....")
def show_magiccians(magaicians):
    for name in magaicians:
        print(name.title())

magaicians = ["harry houdini","david blaine","teller"]
show_magiccians(magaicians)

#8-10
'''
def show_magicians(magicians):
    """打印列表中每个魔术师的名字。"""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """在每个魔术师的名字中都加入字样the Great。"""
    # 新建一个列表，用于存储修改后的魔术师名字。
    great_magicians = []

    # 在每个魔术师的名字中都加入字样the Great，并将其添加到great_magicians中。
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # 将修改后的名字放回到列表magicians中。
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)
print("\n")
make_great(magicians)
show_magicians(magicians)
'''


#8-11

def show_magicians(magicians):
    """打印列表中每个魔术师的名字。"""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """在每个魔术师的名字中都加入字样the Great。"""
    # 新建一个列表，用于存储修改后的魔术师名字。
    great_magicians = []

    # 在每个魔术师的名字中都加入字样the Great，并将其添加到great_magicians中。
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # 将修改后的名字放回到列表magicians中。
    for great_magician in great_magicians:
        magicians.append(great_magician)
    return magicians

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

#副本，切片表示法[:],创建副本，函数传递的副本可保留原始列表的内容,副本可用于修改
print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

#任意传递参数的实参 *toppings
print("\n元组 ")
def make_pizza(*toppings):
    for pizza in toppings:
        print(pizza)

make_pizza("pepperoni")
make_pizza("mushrooms","green peppers","extra cheese")

#综合使用位置实参和任意数量参数
def make_pizza(size,*toppings):
    '''概述要制作的披萨'''
    print("\nMaking a " + str(size))
    for pizza in toppings:
        print("-" + pizza)
make_pizza(23,"perp")
make_pizza(35,"green peppers","extra cheese")