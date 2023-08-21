class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduation_year=year
x=student("dev","raj",2023)
print(x.printname(),x.graduation_year)