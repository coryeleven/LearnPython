x = set('abcd')
y = set(['a','b','c','de','cf',10])
print(x,y)

#取交集
print(x & y)
#取并集
print(x|y)
#取差集，表示x里有，y里没有的
print(x-y)
#取对称差集（项在x或y中，但不会同时出现现在二者中）
print(x^y)

a = (1,2,3,4,5,6,7,8,0,1,2,2,4,4,5)
print(a)
#去除重复的元素
print(set(a))

#set 去除重复的列表
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
for lang in set(favorite_languages.values()):
    print(lang)


