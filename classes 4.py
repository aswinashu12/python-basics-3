class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def __str__(self):
        return f"({self.name},{self.age},{self.salary})"
p1=employee("cilian",48,120000)
p2=employee("murphy",51,100000)
p3=employee("robert",47,200000)
p4=employee("downey jr",56,300000)
print(p1)
print(p2)
print(p3)
print(p4)