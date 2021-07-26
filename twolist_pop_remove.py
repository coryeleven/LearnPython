# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 6:53 下午
# @File    : twolist_pop_remove.py
# @Description :在两个列表之间移动元素，使用pop,remove操作元素

#在两个列表之间移动元素，使用pop,remove操作元素
unconfirmed_users = ['alice','brain','candace']
cofirmed_users = []
print('before unconfirmed_users :',unconfirmed_users)
print('before cofirmed_users :',cofirmed_users)
while unconfirmed_users:
    cofirmed_user = unconfirmed_users.pop()
    print("Verifying user: " + cofirmed_user.title())
    cofirmed_users.append(cofirmed_user)
print("The following users have been confirmed: ")
for cofirmed_user in cofirmed_users:
    print(cofirmed_user.title())
print('after unconfirmed_users :',unconfirmed_users)
print('after cofirmed_users :',cofirmed_users)

#remove
pets = ['cat','dog','cat','goldfish','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#使用用户来填充字典
# reponse = {}
# polling_active = True
# while polling_active:
#     name = input("\n" + "what's your name ?")
#     reponseinfo = input("Which mountaion would you like ro climd somday ?")
#     reponse[name] = reponseinfo
#     repeat = input("\n" + "Would you like to let another person repond? (Yes/No)")
#     if repeat == "No":
#         polling_active = False
# print("\n--- Poll Results---")
# for name,responses in reponse.items():
#     print(name + " would you like to climb " + responses + ".")


#7-8
sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

#7-9
sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("\n")
    while sandwich_orders:
        current_sandwich = sandwich_orders.pop()
        print("I'm working on your " + current_sandwich + " sandwich.")
finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

#7-10
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

responses = {}
while True:
    name = input(name_prompt)
    place = input(place_prompt)
    responses[name] = place
    repeat = input(continue_prompt)
    if repeat != "Yes":
        break
print("\n--- Results ---")
for name,place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")
