# fizzBuzz exercise with if else condition 
a = int(input('Enter a number: '))
if a % 3 == 0 and a % 5 == 0:
    print('FuxxBuzz')
elif a % 3 == 0:
    print('Fizz')
elif a % 5 == 0:
    print('Buzz')
else:
    print(a)


# Fizzbuzz with function 
def fizzBuzz(input):
    if input %3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizzBuzz(15))