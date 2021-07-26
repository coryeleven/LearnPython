#关键字with 在不需要访问文件后将其文件关闭
#open 函数
with open("1txt", encoding='utf-8') as file_object: #将文件内容存在变量file_object中
    contens = file_object.read()
    #rstrip 删除空白
    print(contens.rstrip())

#\\反转  \t失败成制表符
file_path = "/\\2test"
with open("/\\2test", encoding='utf-8') as file_object:
    contens = file_object.read()
    print(contens)


#逐行读取
with open(file_path,encoding='utf-8') as file_object:
    for conten in file_object:
        print("逐行读取 :")
        print("\t " + conten.rstrip())


#使用文件内容

with open("1txt") as file_number:
    #readlines 读取文件的每一行
    lines  = file_number.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
print(pi_string[:50] + "....")
print(len(pi_string))

# birthday = input("Enter your birthdat,in the from mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appers in the first million digits of pi!")
# else:
#     print("Your birthday does not  appers in the first million digits of pi!")

#10-1
print("\n10-1 练习笔记")
with open("pro.txt") as file_pro:
    #读取整个文件
    # contens = file_pro.read()
    # print(contens)

    #遍历循环读取文件
    # for i in file_pro:
    #     print(i)

    #存储在一个变量中，遍历读取文件
    # lines = file_pro.readlines()
    # for line in lines:
    #     print(line.strip())


#10-2
    lines = file_pro.readlines()
    for line in lines:
        #replace 替换
        print(line.rstrip().replace("Python","java"))
