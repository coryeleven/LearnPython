import json
def get_stored_username():
    '''如果username 存在，读取'''
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return  None
    else:
        return username

def greet_user():
    '''问候用户，并指出名字'''
    username = get_stored_username()
    if username:
        print("Welcom to back: " + username + "!")
    else:
        username = input("What's your name?\n")
        filename = "username.json"
        with open(filename, 'w') as f_w:
            json.dump(username, f_w)
            print("We'll remember you when you com back, " + username + "!")
def get_new_username():
    '''提示用户输入用户名'''
    username = input("What's your name?\n")
    filename = "username.json"
    with open(filename, 'w') as f_w:
        json.dump(username, f_w)
        print("We'll remember you when you com back, " + username + "!")

greet_user()
