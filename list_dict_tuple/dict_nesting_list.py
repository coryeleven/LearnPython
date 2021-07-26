# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 6:23 下午
# @File    : dict_nesting_list.py
# @Description : 字典嵌套列表

#字典列表 嵌套
print("\n")
aline_0 = {'color':'green','points':5}
aline_1 = {'color':'yellow','points':10}
aline_2 = {'color':'red','points':15}
aliens = [aline_0,aline_1,aline_2]
print(aliens)
for a in aliens:
    print(a)


#追加字典
aliens = []
for aliens_number in range(0,30):
    new_aliens = {'color':'green','points':aliens_number,'speed':'slow'}
    aliens.append(new_aliens)
print(aliens)
for alien in aliens[:5]:
    print(alien)
print('Total number of aliens :' + str(len(aliens)))

#创建一个用户存储外星人的列表
print('\n')
aliens = []
for alien_name in range(0,20):
    new_alien = {'color':'red','points':5,'speed':'slow'}
    aliens.append(new_alien)
print(aliens)
for alien in aliens[0:3]:
    if alien['color'] == 'red':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['spedd'] = 'medium'
    elif alien['color'] == 'red':
          alien['color'] = 'green'
          alien['points'] = 15
          alien['spedd'] = 'fast'
for alien in aliens[0:5]:
    print(alien)
print('....')

#字典中嵌套一个列表
#列1
pizza = {
    'crust': 'thick',
    'topping': ['mushrooms','extra cheese']
}
print("You ordered a " + pizza['crust'] + '- crust pizza' +
      'with the folling toppings:')
for topping in pizza['topping']:
    print('\t'+ topping)
#列2
favorite_languages = {
    'jen':['python','ruby'],
    'sarch':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}
for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' + language)