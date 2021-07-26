import xml.sax

class MenuHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentDate = ""
        self.name = ""
        self.price = ""
        self.description = ""
        self.calories = ""

    def startElement(self,tag,attributes):
        if tag == "breakfast_menu":
            print("这是一个早餐的菜单")
            year = attributes["year"]
            print(f"年份 {year}\n")

    def characters(self,content):
        if self.CurrentDate == "name":
           self.name = content
        elif self.CurrentDate == "price":
            self.price == content
        elif self.CurrentDate == "description":
            self.description == content
        else:
            pass

    def endElment(self,tag):
        if self.CurrentDate == "name":
           print(f"name:{self.name}")
        elif self.CurrentDate == "price":
            print(f"price:{self.price}")
        elif self.CurrentDate == "description":
            print(f"description:{self.price}")
            self.description = ""
        elif self.CurrentDate == "calories":
            print(f"calories:{self.calories}")
        else:
            pass
        self.CurrentDate = ""
if __name__ == "__main__":
    parser = xml.sax.make_parser()
    Handler = MenuHandler()
    parser.setContentHandler(Handler)
    parser.parse("example.xml")