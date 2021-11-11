# Import random class
import random

# Receiving/assigning variables & seed value
seed_value = int(input("What seed should be used? "))
random.seed(seed_value)
lower = int(input('What is the lower bound?'))
upper = int(input('What is the upper bound?'))

# Creating loop statement & condition
while lower > upper:
    print('Lower bound must be less than upper bound.')

    # Receiving user input and assigning variable
    lower = int(input('What is the lower bound?'))
    upper = int(input('What is the upper bound?'))

# Assigning variable for number to win game
rand_num = random.randint(lower, upper)
user_quits = 00
# Receive user input and assigning to variable for guess at winning number
user_guess = int(input('What is your guess?'))

# Creating loop statement & conditions
while user_guess != user_quits:

    # Creating if, if else, and if else statements with conditions for output
    if user_guess < rand_num:
        print('Nope, too low.')
        user_guess = int(input('What is your guess? '))
    elif user_guess > rand_num:
        print('Nope, too high.')
        user_guess = int(input('What is your guess? '))
    elif user_guess == rand_num:
        print('You got it!')
else:
    # user_guess == rand_num
    print('You have quit the game. Thank you for playing')

