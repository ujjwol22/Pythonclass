# Assignments 
# Program to Check if a Number is Positive, Negative or 0
x = int(input('Enter a number: '))
if x == 0:
    print('User input is 0')
elif x > 0:
    print('user input positive number')
else:
    print('user input negative number')

# Program to Check if a Number is Odd or Even
x = int(input('Enter a number: '))
if x % 2 != 0:
    print('user input odd number')
else:
    print('user input is even number')

# Program to Take in the Marks of 5 Subjects and Display the Grade
i = 0
sum = 0
while i < 5:
    marks = int(input('Enter a mask of any five subject: '))
    i += 1
    sum += marks
    print(f'user inpur marks are: {marks}')
print(f'total marks is: {sum}')
grade = sum / 5
if grade >= 90:
    print(f'you have got an A+ grade with percentage of {grade}')
elif grade >= 80:
    print(f'you got a B+ grade with percentage of {grade}')
elif grade >= 70:
    print(f'you got a C+ grade with percentage of {grade}')
elif grade >= 60:
    print(f'you got a D+ grade with percentage of {grade}')
else:
    print('Your garde is below D+')

# Program to Find the Sum of Natural Numbers with while loop 
sum  = 0
i = 0
x = int(input('Enter a number to print the sum of your enter natural number: '))
while i< x:
    i += 1
    sum += i
    print(sum, end=' ')
print(f'\nThe sum of natural number is: {sum}')


#sum of first n natural numbers with for loop 
sum = 0
x = int(input('Enter a number to sum up it first natural number: '))
for i in range(1, x+1):
    sum += i
print(sum)