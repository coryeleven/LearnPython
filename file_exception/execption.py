import  json

#10-6 加法运算
"""
print("Please input two number\n")
try:
    x = int(input("first number:\n"))
    y = int(input("second number:\n"))
except ValueError:
    print("Sorry, I really needed a number.")
else:
    sum = x + y
    print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")

#10-7

print("Enter 'q' at any time tu quit . \n ")
while True:
    try:
        x = int(input("first number:\n"))
        if x == 'q':
            break
        y = int(input("second number:\n"))
        if y =='q':
            break
    except  ValueError:
        print("Sorry, I really needed a number.")
    else:
        sum = x + y
        print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
"""
#10-8
with open("cats.txt", 'w') as cats:
    cats.write("henry\n")
    cats.write("clarence\n")
    cats.write("mildred\n")

with open("dogs.txt", 'w') as cats:
    cats.write("willie\n")
    cats.write("annahootz\n")
    cats.write("summit\n")

file_name = ['cats.txt','dogs1.txt']
for filename in file_name:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.readlines()

    except FileNotFoundError:
        pass
    else:
        for o in contents:
            print("\t\t" + o.title().rstrip())
#10-10 使用count 统计单次出现了多少次
line = "Row,row,ROW,RO,bot"
print(line.count("row"))
print(line.lower().count("row"))


#10-11喜欢的数字
number = input("What's your favorite number?")
with open("favorite_number.json", "w") as f_favorite:
    json.dump(number,f_favorite)
    print("Thanks! I'll remember that.")

#10-12 记住喜欢的数字
try:
    with open("favorite_number.json") as f_w:
        number = json.load(f_w)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open("favorite_number.json", "w") as f_w:
        json.load(number,f_w)
    print("Thanks,I'll remember that")
else:
    print("I know your favorite number! It's " + str
    (number) + "..")