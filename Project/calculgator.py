import math
print('1. Addition')
print('2. Subtraction')
print('3. Division')
print('4. Floor Division')
print('5. Multiplication')
print('6. Exponential')
print('7. SquareRoot')
print('8. Modulo')
print('9. expression')
print('10.cube')
print('11. greatest number')
print('12. positive or negative')
intake = int(input('Enter your required option: '))

if intake==1:
    print('\nEnter a value for Addition')
    first = float(input('Enter a number: '))
    second= float(input('Enter a number: '))
    addition = first + second
    print(f'Addition of {first} and {second} is {addition}' )

elif intake == 2:
    print('\nEnter a value for Subtraction')
    first = float(input('Enter a number: '))
    second= float(input('Enter a number: '))
    subtraction = first - second
    print(f'Difference of {first} and {second} is {subtraction}')

elif intake == 3:
    print('\nEnter a value for Division')
    first = float(input('Enter a number: '))
    second= float(input('Enter a number: '))
    division = first / second
    print(f'Division between {first} and {second} is {division}' )

elif intake == 4:
    print('\nEnter a value for Floor Division')
    first = float(input('Enter a number: '))
    second= float(input('Enter a number: '))
    floordivision = first // second
    print(f'Division between {first} and {second} is {floordivision}')

elif intake == 5:
    print('\nEnter a value for Multiplication')
    first = float(input('Enter a number: '))
    second= float(input('Enter a number: '))
    multiplication = first * second
    print(f'Multiplication between {first} and {second} is {multiplication}')

elif intake == 6:
    print('\nEnter a value for Exponential')
    first = float(input('Enter a number: '))
    second= float(input('Enter a number: '))
    # Exponential = math.pow(first, second)
    Exponential = first ** second
    print(f'Exponential of {first} and {second} is {Exponential}')

elif intake == 7:
    print('\nEnter a value for SquareRoot')
    first = float(input('Enter a number: '))
    second= float(input('Enter a number: '))
    squareroot =  math.sqrt(first)
    squareroot1=  math.sqrt(second)
    print(f'The square root of {first} is {squareroot} and {second} is {squareroot1}')

elif intake == 8:
    print('\nEnter a value for modulo')
    first = float(input('Enter a number: '))
    second= float(input('Enter a number: '))
    modulo = first % second
    print(f'The modulo / remainder of {first} is {modulo}, when it is module by {second}')

elif intake == 9:
    print('\nEnter a value evaluate expression')
    first = eval(input('Enter evaluate expression l1: '))
    second= eval(input('Enter evaluate expression l2: '))
    print(f"The result of evalate expression l1 is {first} and l2 is {second}")

elif intake == 10:
    print("\nEnter a cube")
    first = float(input('Enter a first number: '))
    cube =  first ** 3
    print(f'The cube of {first} is {cube}')

elif intake == 11:
    print('\nEnter a number to find the greatest number: ')
    first = float(input('Enter a first number: '))
    second = float(input("Enter a second number: "))
    third = float(input('Enter a third number: '))
    if first > second > third:
        print(f"{first} is greatest number")
    elif second > first > third:
        print(f"{second} is greatest number")
    else:
        print(f"{third} is greatest number")

elif intake == 12:
    print('\nEnter a number to see either it is positive or negative: ')
    first = float(input("Enter a number: "))
    if first > 0:
        print('Positive number')
    elif first == 0:
        print('Neutral Number')
    else:
        print('Negative number')
else:
    print('\n')
    print('sorry! \ninvalide option')