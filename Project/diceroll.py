# game of dice 
import random
def dice(start=1, end=6): 
    '''this function is created to generate a random int number to make a dice rolling game '''
    a = random.randint(start, end)
    z = random.randint(start, end)
    return a, z

roll_again = 'yes'

while roll_again == 'yes' or roll_again == 'y':
    print('Rolling the dice....')
    x = dice(1, 6)
    print(f'the dice value is: {x}')
    roll_again = input('Do you want to roll a dice again? (yes/no): ')
    if roll_again == 'n' or roll_again == 'no':
        break