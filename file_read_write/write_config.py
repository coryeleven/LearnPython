import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {
    "ServerAliveInterval" : "45",
    "Comperssion":"Yes",
    "CompressionLevel":"9",
}
config["bitbucket.org"] = {}
config["bitbucket.org"]["User"] = "hg"
config["topsecret.server.com"] = {}
topsecret = config["topsecret.server.com"]
topsecret["Port"] = "59002"
topsecret["ForwardX11"] = "no"
config["DEFAULT"]["ForwardX11"]="yes"
with open("pip.ini","w") as configfile:
    config.write(configfile)
with open("pip.ini","r") as f:
    print(f.read())