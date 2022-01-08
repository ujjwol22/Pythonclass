# password authentication 
import getpass # it dpesnot show how the password that we enter 
import pwinput # when we enter a password it will comvert to astric 
# importing model 
database = {'Ujjwol.parajuli':'456', 'sujwol.parajuli':'123'} # creating a dictionary and storing keys and value 
username = input('Enter your name: ') # userinput for username 
for i in database.keys():
    # print(i)
    if username == i:
        # password = getpass.getpass("Enter your password: ")
        password = pwinput.pwinput("Enter your password: ")
        if password == database[i]:
            print('Account is activated!')
            break
        else:
            print("Password couldnot match!")
            break
    else:
        continue # if the 1st key:vlaue is not found in i = 1 condition then it will continue again 
else:
    print('Username is not found!')
    