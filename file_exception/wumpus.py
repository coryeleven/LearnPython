from random import  choice


cave_numbers = range(1,21)
#choice() 方法返回一个列表，元组或字符串的随机项
wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while player_location == wumpus_location:
    player_location = choice(cave_numbers)
print("Welcom tu Hun the Wumpus!")
print("You can see " + str((cave_numbers)) +",caves")
print("To play, just type of number ")
print("of the cave you wish to enter next")

while True:
    print("You are in caver ", + player_location)
    if (player_location == wumpus_location + 1 or  player_location == wumpus_location - 1 ):
        print("I smell a wumpus!")
    print("Wihch cave next!")
    player_input = input(">")
    # isdigit() 方法检测字符串是否只由数字组成。
    if (not player_input.isdigit() or int(player_input) not in cave_numbers):
        print(player_input + ", is not a cave..")
    else:
        player_location = int(player_input)
        if player_location == int(player_input):
            print("Aargh ! You got eaten by a wumpus !")
            break