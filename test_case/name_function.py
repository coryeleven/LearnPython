def get_formatted_name(first,last):
    """生成一个整洁的名字"""
    full_name = first + " " + last
    return  full_name.title()

def city_country(city,country):
    """返回一个'Santiago, Chile'的字符串"""
    return (city.title() + " " + country.title())


def city_countrys(city,country,population):
    """返回一个形如'Santiago, Chile - population 5000000'的字符串。"""
    return (city.title() + "," + country.title() + " - population " + str(population))
