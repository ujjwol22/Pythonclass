# Gui password generator 
import random 
from tkinter import *
import string 

def generate_Password(num):
    password = []
    for i in range(16):
        x = random.randint(0, 94)
        password += string.printable[x]
    # return password
    
    lbl.config(text=password)

# print(generate_Password(16))

root = Tk()
root.title('PASSWORD GENERETOR')
root.geometry("100x100")
btn = Button(root, font = ('times', 15, 'bold'))
btn.grid(row = 2, column=2)
lbl = Label(root, font=('tuime', 15, 'bold'))
lbl.grid(row = 4, column = 2)
root.mainloop()