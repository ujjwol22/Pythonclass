# string are immutable which cant be chage 
# example of immutable 
a = 'hello'
a[4] = 'y' # this is immutable, where we cant change the character of the string 
print(a[4])

# creating a string 
a = 'string'
print(a)

# single quotation 
a = 'hello python programmer'
print(a)

# double quotation 
a = "hello python programmer"
print(a)

# tripe quotation 
a ='''hello....
python....
programmer....'''
print(a)
# ACCESSING THE character in string 
a = 'python programming'
print(a[0]) # gives first value 
print(a[-1]) # gives last value
# string sclicing 
# range of character in that string 

# syntax: string_name[start: end : step]
a = 'pythonprogramming'
print('print from position 0 to 10: ', a[0:10])
print('print from position 0 to 10 in step of 2: ', a[0:10:2])
print('print from position 0 to end in step of 2: ', a[0: :2])
print('print from position 0 to end: ', a[6: ])
print('print from position 6 to 13: ', a[6:13])

# at the time of - value 
a = 'hello python programmers '
print(a[-9: -2]) # always start from big digit and end with small, because -2 is near to 0 than -9. 

# deleting/updating from string 

# Deleting the string 
a = 'hello'
del a # deleting the string with del keyword 
# print(a) # this throw an error because there is no value as we already
#  deleated 'a' 

# updating / re-assign the stting
a = 'python program' # updating the a with new string  
print(a)

# escape sequencing 
a = '''hey i'm ujjwol "from lalitpur"'''
print(a) # multi use of quotation 
b = 'hey i\'m ujjwol from \"lalitpur\"' # scape sequence 
print(b)
w = "https:\\\\www.google.com"
print(w)
x = r'hey i\'m ujjwol from \"lalitpur\"' # 'r' ignores the escape sequence and 
# return as it is 
print(x)

# formated mathod 
a = 'python'
b = 'programming'
c = 'Django'
s = "{} {} {}".format(a, b, c)
print(s)

# we can manipulate it as we like 
s = "{} {} {}".format(b, c, a) # manipulated 
# s = "{} {} {}".format(b, a) # throws an orror because it a functio and have 
# to pass all the value as we define with {} 
print(s)

# positional format
# i love doing python programming in Django
s = "i love doing {0} {1} in {2}".format(a, b, c) # positional formating  
print(s)

# format method 
x = 'i love {} {} and {} framework {}'.format(a, b, c, b)
print(x)

# f-string
y = "{l} {f} {g}".format(l = 'hey', f = 'how are u?', g = 'python...')
print(y)        

# python string operation concatenation 
a = 'hello'
b = 'do you like programming in python?'
c = a + ' ' + b
print(c)
# using comma(,) : comma gives a single white space 
var1 = 'hello'
var2 = 'world'
print(var1, var2)

# using comma(,) : comma gives a single white space 
var1 = 'hello'
var2 = 'python programmer....'
print(var1, var2)
# using comma(,) : comma gives a single white space 
var1 = 'hello'
var2 = 'world'
print(var1, var2)

# using comma(,) : comma gives a single white space 
var1 = 'hello'
var2 = 'python programmer....'
print(var1, var2)
# iterating throuth string 
a = 'hellopythonprogrammers'
for i in a:
    print(i, end=' ')
    
# using range len() function 
a = 'hellopythonprogrammers'
for i in range(0, len(a)):
    print(a[i], end=' ') # iterating a string 'a'
# revision/recall range 
a = range(0, 5)
print(a) # as range is assign in a 
# to iterate through a value of range 
for i in a:
    print(i, end=' ')    
print(type(a))
# enumurate() is a advance looping function 
# enumerate gives a index and value, but its is always our choice to print as we like i.e. index, value.
string = 'python'
# inxed, value
for index, value in enumerate(string):
# for i, v in enumerate(string):
    print(index, end='') # index of string value 
    print(value, end=' ') # value that is in string
# enumurate() is a advance looping function 
# enumerate gives a index and value, but its is always our choice to print as we like i.e. index, value.
string = 'python'
# inxed, value
for index, value in enumerate(string):
# for i, v in enumerate(string):
    print(index, end='') # index of string value 
    print(value, end=' ') # value that is in string
# iterating over a particular elements 
# to reverse string 
a = 'pythonprogrammer'
print(a)
r = a[::-1] # this simply reverse the string 
print(r)
for i in a[::-1]:
    print(i, end=' ') # reversing the stfing using loop 

# reverse string with reversed()
print('')
for i in reversed(a):
    print(i, end=' ') # revers the string using reversed function 

print()
for i in reversed(r): # we have reverse the vlaue of a in r 
    print(i, end=' ') # re-reversing the reverse value


# itereting over a particular element 
a = 'pythonprogramming'
r = a[:8:2]
print(r)

# running above code in loop 
for i in a[6:13:]:
    print(i, end='')

print()
for i in a[::2]:
    print(i, end='')
# string membership test 
a = 'pythonprogramming' 
t = 'p'
q = 'z'
print(t in a) # is present certain string or not 
print(q not in a)  # z is not prsent in string a
# empty string is always a false 
a = ''
# non empty string is always a true 
b = ' '
c = 'print'
print(a and b) # the first condition is false so it will print a same false value 
print(repr())
print(a or c) # print the true value

# repr() : repr is used to print the string along with the quotes
str1 = '' # empty string 
str2 = 'python'
print(repr(str1 and str2))
print(repr(str1 or str2))

str1 = 'for'
print(repr(str1 and str2))
print(repr(str2 and str1))
print(repr(str1 or str2))
print(repr(str2 or str1))

str1 = 'geeks'
print(repr(str1))
print(repr(not str1)) # return true or false 

str1 = ''
print(repr( not str1)) # true
# spliting a string in python 
x = 'hello programmers'
y = x.split() # default split string on the basis of space 
print(y)
print(type(y)) # makes an list 

x = 'hello-programmers-what-are-you-doing?'
y = x.split('-') # spliting the string on the basis of -
print(y)
# find 
str1 = "hello pro for pro programmers"
str2 = "pro"
print(str1.find(str2, 4)) # it looks from left-right
# rfund() function 
str1 = "hello pro for pro programmers"
str2 = "pro"
print(str1.rfind(str2, 4)) # it looks from right-left
# find and rfind
str1 = "hello pro for pro programmers"
str2 = "pro"
print(str1.find(str2, 4)) # it looks from left-right
print(str1.rfind(str2, 4)) # it looks from right-left
# starts with and ends with 
# start with return true or false value 
a = 'hello'
b = 'hello boss'
print(a.startswith(b)) # a start with b? No
# ends with 
a = 'welcome to world largest python programming campaign'
b = 'campaign'
print(a.endswith(b)) # a end with b? yes
# islower()
str1 = 'python programming is BEST'
str2 = 'PYTHON IS BEST language TO LEARN'
print()
# print(str2.lower()) # it convert to lower string 

# lowercase 
print()
if str1.islower():
    print(f'yes the string is in lowercase: {str1}')
else:
    print(f'no the string are not in lowercase: {str1}')
    if str1!= str1.upper():
        print(f"the string is converted to uppercase: {str1.upper()}")
    else:
        print(f'the string is already in uppercase: {str1}')

# uppercase
print()
if str2.isupper():
    print(f'the character is string and uppercase: {str2}')
else:
    print(f'No the character are not uppercase: {str2}')
    if str2 != str2.upper():
        print(f'the string is converted to lower case: {str2.lower()}')
# lower() function
a = 'HELLO THIS IS STRING CONVERSION TO LOWER CASE'
print(a.lower())
# upper() function
a = 'hello this is string conversion to uppercase'
print(a.upper())
# checking either the condition islower or isupper case 
a = 'hello'
if a.islower():
    print(f'Convert to upper: {a.upper()}')
else:
    print(f'convert to lower: {a.lower()}')
# title() function
a = 'hello this is python programmer'
print(a.title())
# len() function
a = 'hello this is python programmer'
print(f'the length of string a is: {len(a)}')
# printing the occurance of "python" in string, 
# prints 2 as it only check till 15th element
str = 'python for Automation and Scriptiong'
print("number of apperance of ""python:"" is: ", end=' ')
print(str.count("python", 0, 15))
# Python code to demonstrate working of
# center(), ljust() and rjust()
str = "Python is the coolest programming language in the world"
# Printing the string after centering with '-'
print ("The string after centering with '-' is : ",end="")
print ( str.center(25,'-'))
# just() in python 
str = "Python is the coolest programming language in the world"
print ("The string after ljust is : ",end="")
print(str.ljust(20, '-'))
# use of just() in python 
str = "Python is the coolest programming language in the world"
print ("The string after rjust is : ",end="")
print(str.rjust(20, '-'))
# isalpha()
a = "hello there..."
b = '123hello'
c = '  '

if (a.isalpha()):
    print('the condition is true and returns a alphabates')
else:
    print('false')
#isnum()
a = "hello there..."
b = '123hello'
c = '  '
if b.isalnum():
    print('the condition is true and returns a alphabates and number')
else:
    print('false')
# isspace()
a = "hello there..."
b = '123hello'
c = '  '
if c.isspace():
    print('the condition is true and will display space')
else:
    print('false')
# join() mathod/ function 
x = 'hey there'
y = 'how are i doing ?'
z = ' '.join([x, y])
z1 = '-'.join([x, y])
print(z)
print(z1)
# python to demostarte the working of strip() 
str = '...hellp programmers how are u doing ?...'
print(str) # display as it is in the string 
print('string after strip all "." is: ', end='')
print(str.strip(".")) # remove all the dots from the string 

# python to demostrate the lstrpi
str = '... hello programmers how are u doing ?...'
print(str)
print('after \'lstrip\': ', end='')
print(str.lstrip('.')) # remove all the dosts from left side 
# python program to demostrate the rtrip 
str = '... hello python programmers how are u doing?'
print(str)
print('after \'rstrip\': ', end='')
print(str.rstrip('.')) # remove all the dots from right side 
# Python code to demonstrate the working of
# max()
 
# printing the maximum of 4,12,43.3,19,100
print("Maximum of 4,12,43.3,19 and 100 is : ",end="")
print (max( 4,12,43.3,19,100 ) )

# python program to demostarte the working od 
# min()
# printing the minimum of 4, 12, 43, 3, 17, 100
print("minimum of 4, 12, 43, 3, 17, 100 is: ", end=' ')
print(min(4, 12, 43, 3, 17, 100))

# Python code to demonstrate working of
# min() and max()
str = "machinelearning"
# using min() to print the smallest character
# prints 'a'
print ("The minimum value character is : " + min(str))
# using max() to print the largest character
# prints 'r'
print ("The maximum value character is : " + max(str))

# python program to demostrate the working condition of 
#  maketrans()
# from string import maketrans fro maketrans()

str = 'artificialintelligence'
str1 = 'gfo'
str2 = 'abc'
# using maketrance () to map elements of str1 to str2
mapping = str.maketrans(str1, str2)
print(mapping)

# python program to demostrate the working condition of 
#  translate()
# from string import maketrans fro translate()

str = 'artificial intelligence'
str1 = 'gfo'
str2 = 'abc'
# using translate() to map elements of str1 to str2
mapping = str.maketrans(str1, str2)
print(str.translate(mapping))

# python program to demostrate the woking of 
# replace()
str = "C++ is a programming language from c++ python was developed."
str1 = 'C++'
str2 = "python"
print('Before replacemet: ', str)
print('after the replacement of string we get: ')
print(str.replace(str1, str2, 1))

# python program to demostrate the working of 
# expandtabs()
string = 'python\tfor\tData Science'

# no parameters, by default size of 8
print(string.expandtabs())

#  tab size taken as 2
print(string.expandtabs(2))

#  tab size taken as 5
print(string.expandtabs(5))
text = 'python for artificial intelligence'

# splits at space 
print(text.split()) 

words = 'python, for, artificial, intelligency'
# splits the word with comma 
print(words.split(','))

word = 'python:for:artificial:intelligency'
# splite on the basis of :
print(word.split(':'))

word = 'catbatratsatfat'
# split on the basis of t
print(word.split())
 # python program to demostarate the working of 
# partition()
string = 'python is best'

# 'is' seperator is found 
print(string.partition('is'))

# 'not' seperator is not found
print(string.partition('not'))

string = 'python is good, isn\' it'

# splits at first occurance of 'is'
print(string.partition('is'))