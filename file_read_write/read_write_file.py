f = open("ad.txt","w",encoding="utf-8")
f.write("测试w写入的，如果文件存在，测清空文件之后创建，如果文件不存在，则创建")
f.close()

f = open("ad.txt","a",encoding="utf-8")
f.write("测试追加")
f.close()

f = open("ad.txt","r",encoding="utf-8")
print(f.read())
print(type(f.read()))
f.close()

# f = open("ad.txt","rb")
# print(f.read())
# data = f.read()
# print(type(f.read()))
# print("将读取的内容解码\n" + data.decode('utf-8'))
# f.close()

# with  open('ad.txt','w') as f:
#     f.write("我是用with写入的，不用关闭close")
with open("ad.txt","rb+") as f:
    f.write(b"aabcdefghijklmn")
    print(f.seek(5))
    print(f.read(1))
    f.seek(-3,2)
    print(str(f.read(1)))