'''
    while 循环，for循环
'''
flag = True
while flag:
    input_str = input("please input something,'q' for quit.-> ")
    print('your input is : %s',input_str)
    if input_str == 'q':
        flag = False
print("you're out of circulation")


'''
    for 循环
'''
sum = 0 
for i in range(10000):
    sum += i
    print(sum) 
print(sum)

