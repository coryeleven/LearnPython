import os,sys
with open('log.txt','w') as f:
    f.write('Hello world\n')
    f.write('Hello world\n')
    f.write('Hello world\n')
    f.write('Hello world\n')

    
with open('log.txt',encoding='utf-8') as read_f,open('log.txt.swap',"w") as write_f:
    for line in read_f: #逐行操作，防止内存溢出
        line = line.replace("world","Cory") 
        write_f.write(line)
        print(line.rstrip())
os.remove('log.txt')
os.rename('log.txt.swap','log.txt')


