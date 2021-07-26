# -*- coding: utf-8 -*-


#面向对象
class Registration:
    def __init__(self):
        self.school = {
            'linux':[],
            'python':[]
        }
    def register(self,magir,student):
        if magir in self.school:
            self.school[magir].append(student)
            print("报名成功")
        else:
            print("Sorry,报名失败，没有这样的课程 %s"%magir)


if __name__ == '__main__':
        stdent = {
            "name": "cory",
            "age": "24",
            "gender": "男",
            "magir": "python"
        }
reg = Registration()
reg.register(stdent.get('magir'),stdent)
print(reg.school)

