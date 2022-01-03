# card game 

# import random
# face_card = {11:'Jack', 12:'Queen', 13:'King', 1:'Ace', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten'}
# card_icon = {1:'Heart', 2:'Club', 3:'Diamond', 4:'Spade'}
# random_card = random.choice(face_card)
# random_icon = random.choice(card_icon)
# print(f"your card is '{random_card}'' of '{random_icon}'") 

import random 
face_card = ['Jack', 'Queen', 'King', 'Ace', 'Two', 'Three', 'Four', 'Five', 'six', 'Seven', 'Eight', 'Nine', 'Ten']
card_icon = ['Heart', 'Club', 'Diamond', 'Spade']

def chose_a_card():
    '''ths function is created to generate a random number inorder to use it for random card ganerating design '''
    card = random.choices(face_card)
    icon = random.choices(card_icon)
    result = f'the {card} of {icon}'
    return result

choose_again = 'yes'
while choose_again == 'y' or choose_again == 'yes':
    result = chose_a_card()
    print(result)
    choose_again = input('Do you want to roll again? (yes/no): ')
    if choose_again == 'n' or choose_again == 'no':
        break