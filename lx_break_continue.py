"""
    break 中断，跳出当前的循环，不再继续执行循环内的语句
    continue 继续,不再执行continue后的循环语句，立即进行下一次循环
"""

print('-------------break---------------')
count = 0 
while count < 5:
    print('aaa',count)
    count += 1 
    if count == 2:
        break
    print('bbb',count)

print('------------continue--------')
count = 0 
while count < 5:
    print('aaa',count)
    count += 1 
    if count == 2:
        continue
    print('bbb',count)