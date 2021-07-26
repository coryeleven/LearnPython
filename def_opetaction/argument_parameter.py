"""
    1.实参形参、位置参数、关键字参数
    2.形参默认值
    3.传递列表
"""


# 形参
def greet_user(username):
    # 函数体
    print("Hello " + username.title() + ".")
greet_user("Cory") #实参调用函数传给函数的信息


#8-1
def display_message():
    msg = "I'm learning to store code in functions."
    print(msg)
display_message()

#8-2
def favorite_book(book):
    print(book.title() + "is one of my favorite books")
favorite_book("python 从入门到实战")

#位置参数
def decribe_pet(animal_type, pet_name):
    print("I have a " + animal_type + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")
decribe_pet("hamster","harry")
#调用多次函数
decribe_pet("Cory","cat")
#关键字实参
decribe_pet(animal_type="Cory",pet_name="dog")

#形参默认值
def decribe_pet(pet_name,animal_type="Duck"):
    print("\nI have a " + animal_type.title() + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")
decribe_pet(pet_name="whille")
decribe_pet("jack")
#传递实参，忽略默认值
decribe_pet(pet_name="Sira",animal_type="hamster")

#位置参数，关键字参数(形参=实参)
decribe_pet("whille")
decribe_pet(pet_name="whille1")
decribe_pet("harry","hamster")
decribe_pet(pet_name="harry",animal_type="hamster")
decribe_pet(animal_type="hamster1",pet_name="harry1")

#8-3
def make_shirt(size, message):
    """指出要制作的T恤什么样。"""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')

#8-4
def make_shirt(size='large', message='I love Python!'):
    """指出要制作的T恤什么样。"""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')
make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')

#8-5
def describe_city(city, country='chile'):
    """描绘城市。"""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)
describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')

#返回值
def get_formatted_name(first_name,last_name):
    '''返回整洁的名字'''
    msg = first_name + " " + last_name
    print(msg.title())
    return msg.title
get_formatted_name("jimi","hendix")

#实参可选
def get_formatted_name(first_name,last_name,middle_name=""):
    print("\n返回整洁的名字")
    if middle_name:
        full_name = first_name, " " + middle_name + " " + last_name
    else:
        full_name = first_name  + " " + last_name
    return  full_name.title()
musician = get_formatted_name("jhon","hooker")
print(musician)


#返回字典
def build_person(first_name,last_name,age=""):
    print("返回一个字典，其中包含一个人的信息")
    perspons = {'first':first_name,"last":last_name}
    if age:
        perspons['age'] = age
    return  perspons
musician = build_person("j","k",12)
print(musician)


#函数结合wihle循环
def get_formatted_name(first_name,last_name):
    print("Return Name")
    full_name = first_name + " " + last_name
    return  full_name.title()
while True:
    print("\nPleast tell your name ?")
    print("(enter 'q' at any time quit)")
    f_name = input("First name :")
    if f_name == "q":
        break
    l_name = input("Last name :")
    if l_name == "q":
        break
    request = get_formatted_name(f_name,l_name)
    print('\nHello, ' + request)
    print(request)

#8-6城市名
def city_country(city_name,country):
    print("返回一个类似于'Santiago, Chile'的字符串。")
    print (city_name.title() + " , " + country.title())

city_country('santiago','chile')

def city_country(city_name,country):
    print("返回一个类似于'Santiago, Chile'的字符串。")
    return city_name.title() + " , " + country.title()

city = city_country('ushuaia','argentina')
print(city)

#8-7 专辑
def make_album(artist, title, tracks=0):
    """创建一个包含专辑信息的字典。"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks #添加键值对
    return album_dict
album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)


#8-8用户的编辑
# def make_album(artist, title, tracks=0):
#     """创建一个包含专辑信息的字典。"""
#     album_dict = {
#         'artist': artist.title(),
#         'title': title.title(),
#         }
#     if tracks:
#         album_dict['tracks'] = tracks #添加键值对
#     return album_dict
# # 生成提示语。
# title_prompt = "\nWhat album are you thinking of? "
# artist_prompt = "Who's the artist? "
#
# # 让用户知道如何退出。
# print("Enter 'quit' at any time to stop.")
# while True:
#     artists = input(title_prompt)
#     if artists == "quit":
#         break
#     titles = input(artist_prompt)
#     if titles == "quit":
#         break
# album = make_album(artists,titles)
# print(album)
# print("\nThanks for respomding!")

#传递列表
def greet_users(names):
    for name in names:
        msg =  "\nHello " + name.title() + "!"
        print(msg)

usernames = ["Ty","boy","girl"]
greet_users(usernames)
