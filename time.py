# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 18:20
# @Author  : 海绵宝宝cory！！
# @FileName: time.py
# @Software: PyCharm
import time
import  os
print(time.localtime()) #九元素 时间

#time.struct_time(tm_year=2021, tm_mon=1, tm_mday=26, tm_hour=18, tm_min=20, tm_sec=53, tm_wday=1, tm_yday=26, tm_isdst=0)
# 年 月 日 时 分 秒（1-61 闰秒） 一周的第几天（0-6） 一个月的第几天 是否夏令时（1：启用，0：不启用，-1：不知道）

print(time.gmtime()) #UTC 时区

print(time.struct_time((2021,1,26,18,22,21,1,26,1)))
print(time.asctime())
print(time.ctime())
# print(time.mktime())
# time.sleep(1)
# print("sleep 1")


print("-----os-----")
# print(dir(os))

# help(os)

print("分隔符" + os.sep) #分隔符
print("操做系统" + os.name)
print("查下看文件所在的目录" + os.getcwd())
list_dir = os.listdir(os.getcwd()) #列出文件所在的目录所有文件
for dir in list_dir:
    print(dir)
# os.chdir('class')
# os.mkdir('cs') #创建目录
# os.makedirs('cs/cs') #创建多个目录
# os.remove('cs.html') #删除文件
# os.removedirs('cs/cs') #删除递归目录
# os.rmdir('cs') #删除目录


# print(os.system("ping 127.0.0.1")) #直接输出
f = os.popen("ping 127.0.0.1") #将结果保存成功文件
for i in f:
    print(i)
# os.chdir('D')
