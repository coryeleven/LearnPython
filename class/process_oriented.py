# -*- coding: utf-8 -*-

#面向过程
"""
    面向过程：核心是过程二字，过程指的是解决问题的步骤，好比如设计一条流水线，是一种机械式的思维方式。
    就是程序从上到下一步步执行，一步步从上到下，从头到尾的解决问题 。
    基本设计思路就是程序一开始是要着手解决一个大的问题，然后把一个大问题分解成很多个小问题或子过程，这些子过程再执行的过程再继续分解直到小问题足够简单到可以在一个小步骤范围内解决。
"""
school = {
    'linux':[],
    'python':[]
}
def regiset(major,stdent):
    #pass
    if major in school:
        school[major].append(stdent)
        print("报名成功")
    else:
        print("Sorry,报名失败！")

if __name__ == '__main__':
    stdent = {
        "name":"cory",
        "age":"24",
        "gender":"男",
        "major":"python"
    }
regiset(stdent.get('major'),stdent)
print(school)

