import sys
import random

def guess():
    first = sys.argv[1]
    last = sys.argv[2]
    real = (random.choice(range(int(first), int(last) + 1)))
    num = input(f'Welcome to the Guessing Game! Guess the magical number between {first} and {last}: \n')

    while True:
        try:
            if int(num) == int(real):
                print(f'Right guess! The magical number is {real}. Congratulations!')
                break
            while int(num) != int(real):
                num = input(f'Wrong guess! Please, try harder:\n')
        except ValueError:
            num = input(f'Please, enter an integer between {first} and {last}:\n')
guess()

# JB-Rockstar
# gokhanbalik8@gmail.com

