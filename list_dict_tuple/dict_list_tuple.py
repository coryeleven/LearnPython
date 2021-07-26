# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 18:28
# @Description: 字典 元组 列表

def list_main():
    #列表[]方括号，使用,号分隔，列表中的数据类型不要求一致
    print("\nI'am list列表")
    sleep_list = [1,2,3,4]
    list1 = ["Google","Python","Huawei"]
    list2 =['a','b','b','d','e']
    list_all = ["all the them",sleep_list,list1,list2]
    print(list_all)
    print("第二个元素是:" + str(list2[2]))
    list2[2] = 13
    print("更新之后第二个元素是:" + str(list2[2]))

def tuple_main():
    #元组，（）小括号，元组是只读的，无法被修改，在定义时元组必须确定下来
    print("\nI'm Tuple 元组")
    t = ("xiaomi","huawei","readme")
    print(t[1])
    # t[1] = "B" #元组不能被修改
    # print(t[1])
    a = ["a","b","c"]
    b = ["b","c","d"]
    t1 = ("e","f",a)
    print(str(t1))
    t1[2][0] = 0 #元组中的列表可以修改
    t1[2][1] = 1
    t1[2][2] = 2
    print(str(t1))
    print(str(t1[2][0]))


def dict_main():
    #字典 键值对（key value）,花括号{}，使用，号分割
    #1：不允许同一个键出现两次，如果有同一个键赋值两次，则最后一个会被记住
    #2：键不可变，所以可以用数字，字符串，元组充当，用列表则不行，即键必须为不可变数据类型
    print("I'am dict 字典")
    dict = {'color':'red',"height":'170cm'}
    print(dict['color'])
    print(len(dict))
    print(str(dict))

if __name__ == '__main__':
   # list_main()
   # dict_main()
   tuple_main()