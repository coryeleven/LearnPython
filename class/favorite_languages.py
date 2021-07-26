#OrderedDict 具有列表和字典的主要优点，在将信息关联起来的同时保留原来的顺序
#9-13
from collections import  OrderedDict
from random import randint
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'Python'
favorite_languages['sarch'] = 'C'
favorite_languages['edware'] = 'ruby'
favorite_languages['phil'] = 'python'
favorite_languages['key'] = 'The first item in a key-value pair in a dictionary.'
favorite_languages['value'] = 'An item associated with a key in a dictionary.'
favorite_languages['conditional test'] = 'A comparison between two values.'
favorite_languages['float'] = 'A numerical value with a decimal component.'
favorite_languages['boolean expression'] = 'An expression that evaluates to True or False.'


for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title())


#9-14
class Die():
    def __init__(self,sides=6):
        self.sides = sides
    def roll_die(self):
        return randint(1,self.sides)

# 创建一个6面的骰子，再掷10次并显示结果。
d6 = Die()
results = []
for rull_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("\n\n10 rollos of a 6-sides die: ")
print(results)

# 创建一个10面的骰子，再掷10次并显示结果。
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)


# 创建一个20面的骰子，再掷10次并显示结果。
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)
x = randint(1,6)
print(x)