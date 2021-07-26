"""
    1.字典 key,values
    2.添加，修改键对值
    3.遍历字典中的所有key,values
"""
#声明一个键值对
alient = {'color':'green','point':5 }
print(alient['color'])
print(alient['point'])
aline_0 = {'color':'red','points':'5'}
newpoint = aline_0['points']
print("You just earend " + str(newpoint) + " points!")

#添加键值对
aline_0['x_position']=0
aline_0['y_position']=100
print(aline_0)

#修改键值对
aline_1={}
aline_1['color']='red'
aline_1['point']='0'
print(aline_1)
aline_1['color']='yellow'
print(aline_1)

#删除键值对
print(alient)
print(alient['color'])
del alient['color']
print(alient)

#类似与对象组成的字典
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
print("serah's favorite language is " +
      favorite_languages['sarah'].title())
for name,language in favorite_languages.items():
    print('\n'+name.title() + "'s" + " favorite language is " + language.title())

#遍历键值对
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}
#遍历字典for 循环
for key,value in user_0.items():
    print("Key：" + key)
    print("Value：" + value)

#遍历字典中的所有键
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
for name in favorite_languages.keys():
    print('name:',name.title())

#遍历字典中的所有值
for name in set(favorite_languages.values()):
    print('name_values:',name.upper())

#6-5
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river,country in rivers.items():
    print("\nThe " + river.title() + "flows through " + country.title())

print("\nThe following rivers are included in this data set:")
for name in rivers.keys():
    print("- " + name.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())

#6-5
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")
print('\n')
coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")





