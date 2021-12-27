# single inheritance 

class Person:
    # parent class => base class => super class 

    # constructor 
    def __init__(self, name):
        self.name = name

        # to get name 
    def getName(self):
        return self.name

        # to check if this person is an employee
    def isEmployee(self)(self):
        return False


# inheritance or subclass (Note: the person is in bracket)
class Employee(Person):
    # child class => sub-class => derive class 

    # here we return true 
    def isEmployee(self)(self):
        return True

emp = Person('yogesh') # an object of Person 
print(emp.getName(), emp.isEmployee(self)())  

emp2 = Employee('Bikky') # an object of Emplotyee
print(emp2.getName(), emp2.isEmployee(self)())