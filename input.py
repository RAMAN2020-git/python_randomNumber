import random

x = random.randint(1,100) 
user_input = int(-1)

while user_input != x:
    user_input = input("Type something to test this out: ")
    if user_input < x:
        print('number is higher')
    if user_input > x:
        print('number is lower')

    if user_input == x:
        print('YOU GOT THE NUMBER!!!')
    else:
        print('wrong number')