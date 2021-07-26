name = "cory"
last_name = "xu"

#1.title 是以首写字母大写的方式显示每个单词
print(name.title())

#2.upper 是将字符传以大写的方式显示
print(name.upper())

#3.lower 是将字符传以小写的方式显示
print(name.lower())

#4.python 使用+号来合并字符传
print("Hello,\n"+ name.title() + "  "+last_name.title())

#5.rstrip 去除字符传末尾的空白
favorite_language='  Python   '
print(favorite_language.rstrip())

#6.lstrip 去除字符传开头的空白
favorite_language1=favorite_language.rstrip()
print(favorite_language1.lstrip())

