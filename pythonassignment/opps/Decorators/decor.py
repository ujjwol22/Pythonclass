# passing function as a argument and returning function 
def decor(fun):
    def inner():
        print('Befor Enhancing: ')
        fun()
        print('After Enhancing')

    return inner # return inner function 
    # return inner() # calling a inner function 

def fun():
    print('i am the function decorated/enhancing')

result_fun = decor(fun)
result_fun()


# using @decor decorator 
print()
def decor(fun):
    def inner():
        print("Befor enhancing: ")
        fun()
        print('After enhancing')
    return inner

@decor
def fun():
    print('i am the function to be decorated / enhancing')

# result_fun = decor(fun) 
# result_fun()

fun() #=> this is decorated / enhanced function 

# single decoration 
print()
def decor(num):
    def inner():
        a = num()
        add = a + 10
        return add
    return inner

@decor 
def num():
    return 10

# num =  decor(num)
print('final output is ')
print(num())


# multi decoration 
print()
def multiply_5(num):
    def inner():
        a = num()
        mul = a * 5
        return mul
    return inner

def add_10(num):
    def inner():
        a = num()
        add = a + 10
        return add
    return inner

@add_10
@multiply_5
# here first 10 * 5 and = 50 will be added to 10 
# working directory will be from below to upper 
def num():
    return 10

print('final output is ')
print(num())



# multi-decoator 
print()
def multiply_10(num):
    def inner():
        a = num()
        mult =  a * 10
        return mult 
    return inner

def add_5(num):
    def inner():
        a = num()
        add = a + 5
        return add
    return inner

def sub_10(num):
    def inner():
        a = num()
        sub = a - 10
        return sub
    return inner

@multiply_10
@add_5
@sub_10
def num():
    return 15
print('final output is ')
print(num())