# python program to demostrate the 
# hybrid inheritance 

# class school:
#     def scl1(delf):
#         print('You are in School.')

# class student1(school):
#     def scl2(self):
#         print('This is student 1.')

# class student2(school):
#     def scl2(self):
#         print('This is student 2.')

# class student3(student1, school):
#     def scl3(self):
#         print('This is student 3.')

# deriver's code 
# object1 = student3()
# object1.scl1()
# object1.scl2()


# another example of hybrid inheritance 
class hospital:

    # costructor 
    def __init__(self, name):
        self.name = name
        print(f'the name of hospital is: {self.name}')

class emeargeancy(hospital):

    # constructor 
    def __init__(self, name):
        super().__init__(name)
        print('Do this hospital have emeargancy ward?')

        
class regulary(emeargeancy):

    def regula(self):
        print('Do this hospital does a regular check up also ?')

class yes(regulary, hospital):

    # /constructor 
    def __init__(self, name):
        super().__init__(name)

    def answer(self):    
        print(f'yes sir in our {self.name} we have both emeargeancy and regular check up.')

# deriving the classes 
object1 = yes('Nepal_Medicity')
object1.regula()
object1.answer()