#!/usr/bin/env python
# coding=utf-8
import os

print("系统相关...")
print(str(os.name))
print(str(os.environ))
# 当前平台的路径分隔符。在windows下，为‘\’，在POSIX系统中，为‘/’。
print(str(os.sep))
# 可替代的路径分隔符，在Windows中为‘/’。
print(str(os.altsep))
# PATH环境变量中的分隔符，在POSIX系统中为‘:’，在Windows中为‘;’。
print(str(os.pathsep))

print('文件与目录操作...')
# 获取当前工作目录，即当前python脚本工作的目录路径
print(os.getcwd())
# 改变当前脚本工作目录；相当于shell下cd
# os.chdir('../test_case')
print(os.system('ls -rtlh'))
# 返回当前目录: ('.')
print(os.curdir)
# 获取当前目录的父目录字符串名：('..')
print(os.pardir)
# 多层递归目录
# os.makedirs('dir2/dir2')
print(os.listdir('./'))
# 递归删除空目录（要小心
# os.removedirs('dir2/dir2')
print(os.listdir('./'))

# os.mkdir('dirname4') #生成单级目录
# os.rmdir('dirname3') #删除单级空目录，若目录不为空则无法删除并报错
# os.listdir('dirname1')   #列出指定目录下的所有文件和子目录，包括隐藏文件
# os.remove('filename')   #删除一个文件
# os.rename("oldname","new")  #重命名文件/目录
print(os.stat('os_demo1.py'))  # 获取文件/目录信息
# 返回path规范化的绝对路径
print(os.path.abspath('os_demo1.py'))
# 将path分割成目录和文件名二元组返回 ('', 'os_demo1.py')
print(os.path.split('os_demo1.py'))
# 返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.dirname('os_demo1.py'))
# 返回path最后的文件名。如果path以／或\结尾，那么就会返回空值。
print(os.path.basename('os_demo1.py'))
print(os.path.exists('os_demo1.py'))  # 如果path存在，返回True；如果path不存在，返回False
# 如果path是绝对路径，返回True
print(os.path.isabs('/Users/cory/Documents/coryeleven/coryeleven_python/LearnPython/os_demo/os_demo1.py'))
# 如果path是一个存在的文件，返回True。否则返回False
print(os.path.isfile('os_demo1.py'))
# 如果path是一个存在的目录，则返回True。否则返回False
print(os.path.isdir('../os_demo'))

# os.path.join(path1[, path2[, ...]]) #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.getatime('os_demo1.py'))  # 返回path所指向的文件或者目录的最后存取时间
print(os.path.getmtime('os_demo1.py'))  # 返回path所指向的文件或者目录的最后修改时间
print(os.path.getsize('os_demo1.py'))  # 返回文件包含的字符数量

print('执行命令...')
# 运行操作系统命令，直接显示结果。但返回值是0或-1，
print(os.system('ls -rtlh'))
# 可以存储命令输出的数据
data = os.popen('ifconfig')
print(data.read())
