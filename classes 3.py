class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunction(self):
        print(" name is " + self.name )
p1=person("amruthendu",21)
p1.myfunction()