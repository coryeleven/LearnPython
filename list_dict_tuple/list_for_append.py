"""
    列表、for循环读取列表、rang函数、列表切片、列表复制
"""
#声明一个列表
magicans = ['alice','david','carolina']

# for 循环
for i in magicans:
    print(i.title() + ",that was a great trick")
    print("I can't wait to see your nexr trick," + i.title() + "\n")

#range函数生成一系列数字
for value in range(1,10): #
    print(value)

#list() 输出一个列表
numbers = list(range(1,5))
print(numbers)

#切片
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])

#切片终止于末尾
print(players[3:])
#-3 代表输出列表中最后三名队员
print(players[-3:])

#遍历切片
print(players)
print("Here are the first three players on my team:")
for player in players[1:]:
    print(player.title())

#复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print("\nMy favrorite foods are:")
print(my_foods)
for i in my_foods[:]:
    print(i)
print("\nMy friend's favorite foods are:")
for i in friend_foods[:]:
    print(i)

my_foods.append('cannoli') #追加一个新的列表元素
friend_foods.append('ice cream')
print("\nMy favrorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

city = ['zhengzhou','guangzhou','shanghai','beijing','shenzhen']
print(city)
print(city[:3])
print(len(city))
print(city[3:4])
print(city[-3:])
