"""
    1.列表切片
    2.追加，删除，修改列表，pop()删除列表,remove 删除一个指定的列表元素
    3.sort 永久性排序，临时性排序
"""
bicycles = ['thek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[2])
print(bicycles[1].title())
print(bicycles[-1].title())
# -1 默认返回最后一个列表元素
message = "My first bicycle wos a  " + bicycles[-1].title() + "."
print(message)

motocycle = ['honda','yamaha','suzuki']
print(motocycle)

motocycle[1] = "sansung"
print(motocycle)
motocycle.append('ducati') #append 追加列表元素
print(motocycle)

motocycle.insert(0,"Cory")  #insert 插入列表元素
print(motocycle)

del motocycle[-1] #del 删除列表中的元素
print(motocycle)

print("--------------------")
poped_motocycle = motocycle.pop() #pop 删除列表元素还能继续使用，del直接删除不可以使用
print(motocycle)
print(poped_motocycle)
print("The last motocycle I owned was a " +  poped_motocycle.title() + ".")

print(motocycle)
name = "Cory"
motocycle.remove(name) #remove 删除一个指定的列表元素
print('\n\t\t A ' + name.title() + 'is too expensive for me ')

name_student = ['a','b','c','d']
print(name_student)
print(name_student.remove('d'))
print(name_student)
name_student.append('bc')
print(name_student)
name_student.insert(0,'xiaoxu')
name_student.insert(3,'3A')
name_student.append('Http')
print(name_student)
print(name_student.pop())
print(name_student)
del name_student[-1]
del name_student[-1]
print(name_student)




