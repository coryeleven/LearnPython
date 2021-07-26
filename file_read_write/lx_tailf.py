# encoding = 'utf-8'
import time,os

with open('log.txt','rb') as f:
    f.seek(0,2) #将光标移动至文件末尾
    while True:
        line = f.read() #实时显示文件新增加的内容
        if line:
            print(line.decode('utf-8'),end= '')
        else:
            time.sleep(0.2)