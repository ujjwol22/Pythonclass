'''
this is a user define module 
where we have define some of the functions and we are calling it in function_and_module.ipynb file 
and we are accessing from there...
happy coding 
'''

#  Program to Find the Sum of Natural Numbers using function
def sum(a):
    '''this function will sum-up the natural number '''
    add = 0
    for i in range(a):
        add += i
        return add

sum(10)
sum.__doc__


# Program to Find the Largest Among Three Numbers using function
def largest(x, y, z):
    '''this function will check the largest number among three numbers'''
    if x>y>z or x >z>x:
        return x
    elif y>z>x or y>x>z:
        return y
    return z

# a = largest(8, 10, 15)
# print(f'{a} is the largest number')
largest.__doc__