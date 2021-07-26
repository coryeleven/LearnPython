# -*- coding: utf-8 -*-
# @Time    : 2021/7/25 3:32 下午
# @File    : argument_many.py
# @Description :使用任意数量的关键字实参

def build_profile(first,last,**user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile("xy","haiche",a="princes")
print(user_profile)


#8-12
def make_sandwich(*items):
    """使用指定的食材制作三明治"""
    print("\nI'll make you a great sandwich:")
    for a in items:
        print(" ...adding " + a.title() + " to your sandwich:")
    print("Your sandwich is ready!")

make_sandwich('roast beef','chedder cheese','letture','honey djjion')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')

#8-14
def make_car(manufacturer, model, **options):
    """创建一个表示汽车的字典。"""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value
    return car_dict
my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)
my_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_accord)
