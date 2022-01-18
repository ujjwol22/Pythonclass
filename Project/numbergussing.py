import random
def guess(x):
    '''this program is design for random number guessing game '''
    random_number = random.randint(1, x) # random function
    guess = 0 # use in while loop to loop until condition wont satisfy 
    chance = 10 # counter 
    print('\nYou have 10 chance to win the game!\nAll the best!')
    while chance > 0:
        guess = int(input(f'Enter a number between 1 to {x}: '))
        print(f'You have attempt for {chance} times')
        if guess > random_number:
            print(f'{guess} is greater than expected!\n')
            chance -= 1

        elif guess == random_number:
            print(f'You meet the required Number i.e.  {random_number} with-in {chance} attempts.')

        else:
            print(f'{guess} is lower than expected!')
            chance -= 1

ask_again = 'yes'

while ask_again == 'y' or ask_again == 'yes':
    result = guess(100)
    print(result)
    ask_again = input('Do you want to roll again? (yes/no): ')
    if ask_again == 'n' or ask_again == 'no':
        print('We are So Sad, that u are going!')
        break