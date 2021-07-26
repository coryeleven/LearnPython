# encoding = utf-8
import copy
object1 = ['while',28,["python","C++","JavaScript"]]
#对象赋值,深复制deepcopy()
object2 = copy.deepcopy(object1)

#打印对象存在内存中的ID
print(f'id of object1 {id(object1)}')
print(object1)
print([id(ele) for ele in object1])


print(f"id of object2 {id(object2)}")
print(object2)
print([id (ele) for ele in object2])


#尝试改为object1,然后看object2 的变化
object1[0] = 'Wiler'
object1[2].append("css")
print('更改object1之后')
print(f"id of object1 {id(object1)}")
print(object1)

print(f"id of object2 {id(object2)}")
print(object2)
print([id (ele) for ele in object2 ])