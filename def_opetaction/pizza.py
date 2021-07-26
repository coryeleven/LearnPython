# 声明一个make_pizza函数，多个参数值
def make_pizza(size,*toppings):
    print("\nMakeing a " + str(size) +
          "-inch pizza with the following toppings:")
    for toping in toppings:
        print("- " + toping)
make_pizza(14,'pep')