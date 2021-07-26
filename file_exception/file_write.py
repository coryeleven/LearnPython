# w写入模式 r 读取模式 a附加模式
with open('pro.txt', 'w') as file_object:
    file_object.write("In Python you can store as much information as you want.\n")
    file_object.write("In Python you can connect pieces of information.\n")
    file_object.write("In Python you can model real-world situations.\n")



with open('pro.txt', "a") as file_object:
    file_object.write("[ ] 列表， 列表是有序集合，访问列表元素，只需访问该元素的位置即可，索引从 0 开始，列表可以修改\n")


#10-3
with open("guest.txt", 'a') as file_object:
    name = input("What's your name?\n")
    file_object.write("\n" + name)

#10-4
print("\nEnter 'quit' when you are finised")
while True:
    name = input("\nWhat's your name: ")
    if name == 'quit':
        break
    else:
        with open("guest.txt", 'a') as file_name:
            file_name.write("\n" + name)
        print("Hi " + name + ",you've been added to the guest book")

#10-5
filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")
