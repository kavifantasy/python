from datetime import datetime
class Employee:
    #class variable
    bonus=5000

    #parameterized contructor
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    #of both str and repr fun str only will exe,if str is not there repr will exe
    #repr will add additional quotes to string
    #repr will print all the decimal precisions but str will print limited no. after decimal
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.empNo
    
    #other means object other than the object ponted by self
    def __add__(self,other):
        return self.salary+other.salary
   
    #Instance non-parameterized  method
    def getSalary(self):
        return self.salary
    
    #Instance non-parameterized  method
    def applyHike(self):
        self.salary=self.salary*1.04
        return self.salary

    #Class parameterized method
    @classmethod 
    def setBonus(cls,amount):
        cls.bonus=amount

    #static methods
    @staticmethod
    def isworkingDay():
        #local variable
        day=datetime.now().strftime("%w")
        if day=='0' or day== '6':
            return False
        else:
            return True

#employee object
emp1=Employee("Goutham",20000)
emp2=Employee("Vk",25000)

#printing emp salary
print(emp1.salary)
print(emp2.salary)

#instance methods
print(emp1.getSalary())
print(emp1.getSalary())

#using class in the place of emp
print(Employee.getSalary(emp1))

#class method
Employee.setBonus(1000)
print(emp1.bonus)

#static method
print(Employee.isworkingDay())

print(emp1)

print(emp1+emp2)