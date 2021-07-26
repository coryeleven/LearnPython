import os
with open('log.txt',encoding='utf-8') as read_f,open('log.txt.swap','w') as write_f:
    data = read_f.read() #全部读入内存中
    data = data.replace('Cory','Siri') #在内存中完成替换
    write_f.write(data)

os.remove('log.txt')
os.rename('log.txt.swap','log.txt')