# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 6:23 下午
# @File    : dict_nesting_dict.py
# @Description :

#在字典中存储字典
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}
for username,user_info in users.items():
    print("\n Username: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name)
    print("\tLocation: " + location.title())

#6-7
print('\n')
people = []
person = {
    'first_name':'eric',
    'last_name':'matthes',
    'age':43,
    'city':'sitka',
}
people.append(person)

person = {
    'first_name':'ever',
    'last_name':'matthes',
    'age':5,
    'city':'sitka',
}
people.append(person)
print(people)
for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    print(name + ", of " + city + ", is " + age + " years old.")
print('....')

#6-8
# 创建一个用于存储宠物的空列表。
pets = []

# 定义各个宠物并将其存储到列表中。
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)
pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# 显示每个宠物的信息。
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))

#6-9
favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'ever': ['mt. verstovia', 'the playground', 'south carolina']
    }
for name,city in favorite_places.items():
    print("\n " + name.title() + "likes the following places:")
    for place in city:
        print("\t " + place.title() )

#6-10
print('\n')
favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
    }
for name,number in favorite_numbers.items():
    print("\n" +  name.title() + "likes the folling numbers:")
    for number in number:
        print("\t" + str(number))

#6-11
cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himilaya',
        }
    }
for city,cityinfo in cities.items():
    country = cityinfo['country'].title()
    population = cityinfo['population']
    mountains = cityinfo['nearby mountains'].title()

    print("\n" + city.title() + 'is in' + country + '.')
    print("  It has a population of about " + str(population) + ".")
    print("  The " + mountains + " mountains are nearby.")
