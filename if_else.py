"""
    1.检查特定的值是否包含在列表中 关键字 in
    2.检查特定的值是否不包含在列表中 关键字 not in
"""
# if == 等于 相等运算符
cars = ['audi','bm2','bora','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
print(car == 'bmw')
print(car.upper() == 'dmb') #变量的值先转换大小写，再进行比较


# != 不等于
requested_topping = 'mushrooms'
if requested_topping != 'mushrooms':
    print("Hold the mushrooms")
else:
    print('Hold the anchovied')

# 小于 大于 小于等于 大于等于
age = 23
print(age < 30)
print(age > 35)
print(age >= 20)
print(age <= 30)

#and 检查多个条件，须同时满足
age1 = 25
print(age > 20 and age1 < 26 and age < 30)

# or 只满足一个条件即可
print(age < 10 or age1 > 400)

# 检查特定的值是否包含在列表中 关键字 in
requested_topping = ['mushrooms','onions','pineapple']
print('mushooms' in requested_topping)
print('onions' in requested_topping)

#检查特定的值是否不包含在列表中 关键字 not in
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(user.title()+ ", you can post a response if you wish.")

# 布尔表达式
game_active = True
can_deit = False
car = 'boro'
print("Is car == 'boro' ? I think True" )
print(car == 'boro')



# if-else 语句
print("\nif-else 语句")
age = 18
if age >= 10:
    print("You are old enough to vote!")
else:
    print("Please register to vote as soon as you turn 18!")


#if-eles-else
age = 20
print("\nif-eles-else")
if age < 5:
    print("You admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your adminssion cost is $10.")


#测试多个条件
requested_topping = ['mushrooms','extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese")
print("Finished making your pizza!")




alien = ['green','red','yellow']
if 'green' in alien:
    print("Get 20 points!")
elif 'yellow' in alien:
    print("Get 10 points!")
elif 'red' in alien:
    print("Get 15 points!")

age = 80
if age < 1:
    print("He is baby!")
elif age >= 2 and age < 4:
    print("He is toddler")
elif age >= 4 and age < 13:
    print("He is child")
elif age >= 13 and age < 20:
    print("He is youth")
elif age >= 20 and age < 65:
    print("He is Adults")
else:
    print("He is Senior")


favorite = ['apple','xiaomi','orange','watermelon']
if 'apple' in favorite:
    print("You really like apple!")
if 'xiaomi' in favorite:
    print("You really like xiaomi!")
if 'orange' in favorite:
    print("You really like orange!")
if 'watermelon' in favorite:
    print("You really like watermelon!")


requested_topping = ['mushrooms','green peppers','extra cheese']

for requested_toppings in requested_topping:
    print("Adding " + requested_toppings + ".")

print("\nFinished making your pizza")

requested_topping = ['mushrooms','green peppers','extra cheese']
for requested_toppings in requested_topping:
    if requested_toppings == 'mushrooms':
        print("\nSorry , we are out of green peppers right now.")
    else:
        print("Adding " + requested_toppings + ".")
print("\nFinished making your pizza")

#确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("\nAdding " + requested_topping + ".")
else:
    print("\nAre you sure you want a plain pizza?")

#使用多个列表
print("\n使用多个列表")
available_topping = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fires','extra cheese']

for mushrooms in requested_toppings:
    if mushrooms in available_topping:
        print("Adding  " + mushrooms + '.')
    else:
        print("Sorry ,wo dont't have " + mushrooms + ".")
print("\nFinished making your pizza!")


#动手试一试
user = ['admin','test','cmbadmin','cory','jick']
for name in user:
    if name  == "admin"  :
        print("\nHello admin,would you like to see a status report?")
    else:
        print("Hello " +  name +",thank you for logging in again")

user = []
if user:
    for name in user:
        if name == "admin":
            print("\nHello admin,would you like to see a status report?")
        else:
            print("Hello " +  name +",thank you for logging in again")
else:
    print("We need to find some users")


current_user = ['cory','jack','jessica','dayland','dell']
new_user = ['cory','dell','xiaomi','oppo','vivo']
for name in new_user:
    if name in current_user:
        print("用户名 " + name.title()+ " 已被使用")
    else:
        print("用户名 " + name.title() + " 未被使用，可以选择")

current_users_lower = [user for user in current_user] #列表解析
print(current_users_lower)


numbers = list(range (1,10))
print(numbers)
for number in numbers:
    if numbers == 1:
        print("1st")
    elif numbers == 2:
        print("2nd")
    elif numbers == 3:
        print("3rd")
    else:
        print(str(number)+"th") #两个变量，一个是str，另一个是list 所以需要用str转一下
