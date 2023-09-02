class sum:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __add__(self,obj_2):
        total=self.price + obj_2.price
        print(total)
obj1=sum("hublot",28)
obj2=sum("shwarz",24)
print(obj1+obj2)