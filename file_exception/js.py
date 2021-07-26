import json
#读取到内存中
number = ['1','4','6']
with open("number.json", 'w') as f_obj:
    json.dump(number,f_obj)


with open("number.json") as f_r:
    print(json.load(f_r))

#dump  load 从内存中

username = input("\nWhat's your name?\n")
filename = "username.json"
try:
    with open(filename) as f_read:
        json.load(f_read)
except FileNotFoundError:
    with open(filename, 'w') as f_w:
        json.dump(username, f_w)
        print("We'll remember you when you com back, " + username + "!")
else:
    print("welcom back, " + username + "!")