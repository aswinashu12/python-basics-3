class addtn:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        print(self.n1+self.n2)
class subtn:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def sub(self):
        print(self.n1-self.n2)
class multp(addtn,subtn):
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def mul(self):
        print(self.n1*self.n2)
x=int(input("enter the 1st variable"))
y=int(input("enter the 2nd variable"))
calcn=multp(x,y)
calcn.add()
calcn.sub()
calcn.mul()



