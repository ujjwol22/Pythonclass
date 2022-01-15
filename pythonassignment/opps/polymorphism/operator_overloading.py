# operator overloading

class student:

    # constructor 
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    # overloading the + operator 
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1, m2)
        return s3

s1 = student(58, 59)
s2 = student(60, 69)
s3 = s1 + s2
print(s3.m1)
print(s3.m2)