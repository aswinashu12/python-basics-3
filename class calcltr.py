class calculator:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        add=self.n1+self.n2
        return add
    def sub(self):
        sub=self.n1-self.n2
        return sub
    def div(self):
        div=self.n1/self.n2
        return div
    def mul(self):
        mul=self.n1*self.n2
        return mul
n1=int(input("enter the 1st dig"))
n2=int(input("enter the 2nd digit"))
z=float(input("chose 1,2,3,4 for add,sub,mul,div resp"))
p1=calculator(n1,n2)
if z==1:
    print(p1.add())
elif z==2:
    print(p1.sub())
elif z==3:
    print(p1.mul())
elif z==4:
    print(p1.div())
else:
    print("invalid")








