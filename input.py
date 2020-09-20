import random

x = random.randint(1,100) 
user_input = int(-1)

while user_input != x:
    user_input = int(raw_input("Type something to test this out: "))
    if user_input < x:
        print('number is higher')
    else:
        print('below 50')