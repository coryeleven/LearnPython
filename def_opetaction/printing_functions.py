# 声明函数，使用pop操作列表
def print_models(unprinted_designs,complete_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        complete_models.append(current_design)
        
def show_models(complete_models):
    print("\nThe following models have been printed！")
    for complete_model1 in  complete_models:
        print(complete_model1)