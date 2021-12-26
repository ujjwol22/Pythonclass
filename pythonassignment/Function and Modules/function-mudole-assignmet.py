# Program to Check if a Number is Positive, Negative or 0 using function
def numberchicking(a):
    '''This function will check the passing number is positive, Negative 
or zero'''
    if a >= 0:
        return 'positive'
    elif a == 0:
        return 'zero(0)'
    else: 
        return 'Negative'

# calling function 
y = numberchicking(5)
print(y)
numberchicking.__doc__



# Program to Check if a Number is Odd or Even using function
def oddEven(x):
    '''This function will check either the given number is even or odd'''
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'
    
y = oddEven(8)
print(y)
oddEven.__doc__


# Program to Find the Largest Among Three Numbers using function
def largest(x, y, z):
    '''this function will check the largest number among three numbers'''
    if x>y>z or x >z>x:
        return x
    elif y>z>x or y>x>z:
        return y
    return z

a = largest(8, 10, 15)
print(f'{a} is the largest number')
largest.__doc__


# Program to Take in the Marks of 5 Subjects and Display the Grade using function
def result(args):
    sum = 0
    for i in range(args):
        a = int(input("Enter a mask: "))
        sum += a
    grade = ((sum) / 500) * 100
    if grade >= 90:
        return 'A+'
    elif grade >= 80 < 90:
        return 'A'
    elif grade >= 70 < 80:
        return 'B+'
    elif grade >= 60 < 70:
        return 'B'
    elif grade >= 50 < 60:
        return 'C+'
    elif grade >= 40 < 50:
        return 'C'
    elif grade >= 30 < 40:
        return 'D+'
z = result(5)
print(f"Yout Grade is: {z}")


#  Program to Find the Sum of Natural Numbers using function
def sum(a):
    '''this function will sum-up the natural number '''
    add = 0
    for i in range(a):
        add += i+1
        print(add)

sum(10)
sum.__doc__



# Program to make a simple calculator using functions
import math
def cal():
    '''this function work as a calcualtor and the works perform by this calculator is shown below'''
    global a, b
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
  
def factorial(a, b):
    x = math.factorial(a)
    y = math.factorial(b)
    print(f'the Factorial of {a} and {b} is {x}, {y}')

def hcf(a, b):
    gcd = math.gcd(a, b)
    print(f'the HCF of {a} and {b} is {gcd}')

def lcm(a, b):
    x = math.lcm(a, b)
    print(f'the LCM of {a} and {b} is {z}')

def addition(a, b):
    sum = a + b
    print(f'sum of {a} and {b} is {sum}')

def subtraction(a, b):
    sub = a - b
    print(f'ths subtraction value between {a} and {b} is {sub}')

def multiplication(a, b):
    mult = a * b
    print(f'the multiplication between {a} and {b} is {mult}')

def divide(a, b):
    div = a / b
    print(f'the division between {a} and {b} is {div}')

def floordivision(a, b):
    fdiv = a //b
    print(f'the floor division between {a} and {b} is {fdiv}')

def exponent(a, b):
    expo = a ** b
    print(f'the exponent between {a} and {b} is {expo}')

def square_root(a, b):
    x = math.sqrt(a)
    y = math.sqrt(b)
    print(f'the square root of {a} and {b} is {x}, {y}')

def modulo(a, b):
    mod = a % b
    print(f'the modulo of {a} and {b} is {mod}')

def cube(a, b):
    x = a**3
    y = b **3
    print(f'the cube of {a} and {b} is {x} {y}')

print('1. Addition')
print('2. Subtraction')
print('3. Division')
print('4. Floor Division')
print('5. Multiplication')
print('6. Exponent')
print('7. Square Root')
print('8. Modulo')
print('9. cube')
print('10. LCM')
print('11. HCF')
print('12. Factorial')
intake = int(input('Enter your required option: '))

if intake==1:
    cal()
    addition(a, b)

elif intake == 2:
    cal()
    subtraction(a, b)
    
elif intake == 3:
    cal()
    divide(a, b)
    
elif intake == 4:
    cal()
    floordivision(a, b)
    
elif intake == 5:
    cal()   
    multiplication(a, b)
    
elif intake == 6:
    cal()
    exponent(a, b)

elif intake == 7:
    cal()
    square_root(a, b)

elif intake == 8:
    cal()
    modulo(a, b)

elif intake == 9:
    cal()
    cube(a, b)

elif intake == 10:
    cal()
    lcm(a, b)

elif intake == 11:
    cal()
    hcf(a, b)

elif intake == 12:
    cal()
    factorial(a, b)

else:
    print('\n')
    print('sorry! \ninvalide option')
cal.__doc__




# weite a program to display the calander from the model 
import calendar
# yy = 2021
# mm = 12

# from user input 
yy = int(input("Enter a year: "))
mm = int(input("Enter a month: "))
# print(datetime.strftime("%X")) 
print(calendar.month(yy, mm))