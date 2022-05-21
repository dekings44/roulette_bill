import random
from tkinter import N



# if ran_side == 1:
#     print('Heads')
# else:
#     print('Tails')

names = input("Give me everyone's name, seperated by a comma and space\n")

name = names.split(", ")
# name1 = len(names.split(", "))
# ran_num = random.randint(0, name1 -1)
ran_choice = random.choice(name)

print(f'Hoolah!! \n{ran_choice} will take the bill for today.')