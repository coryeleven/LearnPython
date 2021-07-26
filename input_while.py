"""
    1.input str、int，求模运算符
    2.while 循环
    3.break continue结束或跳出循环
"""

#存储成一个变量提示信息 int
'''
prompt = "If you tell us who are you , we can personalize the message you see."
prompt += "\nWhat is your first name?\n"
name = input(prompt)
print(name)
height = input("How tall are you, in inches? ")
height = int(height)   #int函数
print(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older!")
'''


#求模运算符
# height = input("How tall are you, in inches? ")
# height = int(height)   #int函数
# if height % 2 == 0:
#     print("\nThe number " + str(height) + " is even.")
# else:
#     print("\nThe number " + str(height) + " is add.")


#7-1
# car = input("What kind of car would you like? ")
# print("Let me see if I can find you a " + car.title() + ".")

#7-2
# party_size = input("How many people are in your dinner party tonight? ")
# party_size = int(party_size)
# if party_size > 8:
#     print("I'm sorry, you'll have to wait for a table.")
# else:
#     print("Your table is ready.")
# print("...")

#7-3
# number = input("Give me a number,please: ")
# number = int(number)
# if number %10 == 0 :
#     print(str(number) + "is a muitple of 10.")
# else:
#     print(str(number) + " is not a multiple of 10.")

# while 循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#while循环 让用户选择时退出
prompt = "\nTell me somthing,and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != "quit":
#     message =input(prompt)
#     if message != "quit":
#         print(message)

# active = True
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#     else:
#         print(message)

#Break 推出循环
while True:
    city = input('prompt:')
    if city == "quit":
        break
    else:
        print("I'd love to go to " + city.title())

#使用continue
current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number%2 == 0:
        print("模余运算:" + str(current_number))
        continue
    print(current_number)

# x = 1
# while x <= 5:
#     x += 1
#     print("\n" + str(x))
#7-4
# while True:
#     topping = input(prompt)
#     if topping != "quit":
#         print("  I'll add " + topping + " to your pizza.")
#     else:
#         break

#7-5
# prompt = "How old are you?"
# prompt += "\nEnter 'quit' when you are finished. "
# while True:
#     age = input(prompt)
#     if age == "quit":
#         break
#     age = int(age)
#     if age < 3 :
#         print(" You get in free!")
#     elif age < 13:
#         print(" Your ticket is $10.")
#     else:
#         print("  Your ticket is $15.")

