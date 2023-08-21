class manager:
    def __init__(self,salary):
        self.salary=salary
    def printdetails(self):
        print("the manager's salary is", self.salary)
class employee(manager):
    def __init__(self,salary,employees):
        super().__init__(salary)
        self.employees=employees
details=employee(64500,51)
print(details.printdetails(),"\n",details.employees)