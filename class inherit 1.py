class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def fullname(self):
        print(self.fname,self.lname)
class student(person):
     pass
x=student("john",36)
x.fullname()
