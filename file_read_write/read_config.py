import  configparser

config = configparser.ConfigParser()
config.read("pip.ini")

print("遍历配置信息：")

for section in config.sections():
    print(f"section is [{section}]")
    for key in config[section]:
        print(f"key is [{key}],value is [{config[section][key]}]")

print("通过键值获取相应的值。。")
print(f"index-url is [{config['global']['index-url']}]")
print(f"trusted-host is [{config['global']['trusted-host']}]")


