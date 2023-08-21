class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
class student(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
x=student("daniel","craig")
x.printname()