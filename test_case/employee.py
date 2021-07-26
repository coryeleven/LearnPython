class Employee():
    def __init__(self,f_name,l_name,salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salray = salary
    def give_raise(self,amount=5000):
        self.salray += amount