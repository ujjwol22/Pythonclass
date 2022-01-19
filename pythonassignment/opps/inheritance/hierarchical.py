# python program to demostrate the 
# hierarchical inheritance 

# Base class 
class Parent:
    
    def func1(self):
        print('This function is in parent class.')

# derive class 1
class child1(Parent):

    def func2(self):
        print('This function is in child 1.')

# derive class 2
class child2(Parent):

    def func3(self):
        print('This function is in chile 2.')

# derive code 
object1 = child1()
object2 = child2()
print('====================>')
object1.func1()
object1.func2()
print()
print('====================>')
object2.func1()
object2.func3()



# example of hirarchicale inheritance 
print()
class base1:
    def base1(self):
        print('this is a base class 1')

class base2(base1):
    def base2(self):
        print('this is a base class 2')

class derive(base2):
    def derive(self):
        print('this is a derive class 1')

obj = derive()
obj.derive()
obj.base2()
obj.base1()