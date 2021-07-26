import json

def get_stored_name():
    """获取已存在文件"""
    file_name = "username.json"
    try:
        with open(file_name) as f_w:
            username = json.load(f_w)
    except FileNotFoundError:
        return  None
    else:
        return  username

def get_new_username():
    """提示输入用户名"""
    username = input("What's your name ?\n")
    file_name = "username.json"
    with open(file_name,"w") as f_w:
        json.dump(username,f_w)
    return  username

def greet_user():
    """基于用户名问候用户"""
    username = get_stored_name()
    if username:
        corrent = input("Are you " + username + " Ok?(y/n)")
        if corrent == 'y':
            print("Welcom back, " + username + "!")
            #return语句意味着打印欢迎回来的消息后，不再执行后面的代码
            return
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")

    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()