class employee:
    def __init__(self,name,age,post):
        self.name=name
        self.age=age
        self.post=post
    def __str__(self):
        return f"({self.name},{self.age},{self.post})"
x=str(input("enter the name"))
y=int(input("enter the age"))
z=str(input("enter the post"))
p1=employee(x,y,z)
p=str(input("enter the name"))
q=int(input("enter the age"))
r=str(input("enter the post"))
p2=employee(p,q,r)
print(p1)

