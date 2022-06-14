from day14_art import logo, vs
from day14_gamedata import data

import random

import os
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      clear = os.system('clear')
   else:
      # for windows platfrom
      clear = os.system('cls')
      

global score
global correct_guess


def game():
    correct_guess = True
    score = 0

    while correct_guess:
        screen_clear()
        print(logo)

        a = data[random.randint(0, len(data)-1)]
        print("Person 'a'")
        print(f"\n{a['name']}")
        print(f"{a['description']}")
        print(f"{a['country']}")

        print(vs)

        b = data[random.randint(0, len(data)-1)]
        while b == a:
            b = data[random.randint(0, len(data)-1)]
        print("Person 'b'")
        print(f"\n{b['name']}")
        print(f"{b['description']}")
        print(f"{b['country']}")

        guess = input("Who do you think has more followers? Type 'a' or 'b': ")

        screen_clear()
        print(logo)

        if guess == 'a':
            if a['follower_count'] > b['follower_count']:
                score += 1
                print(f"You are correct! Your current score is {score}")        
            else:
                print(f"You are wrong! Your final score is {score}")
                correct_guess = False
        elif guess == 'b':
            if a['follower_count'] < b['follower_count']:
                score += 1
                print(f"You are correct! Your current score is {score}")    
            else:
                print(f"You are wrong! Your final score is {score}")
                correct_guess = False
        else:
            print("You have typed anything other than 'a' or 'b' !")
            print(f"Your final score is {score}")
            correct_guess = False
        input("Press Enter to continue...")


print(logo)
print("\nWelcome to the Higher Lower Game!")
print("\nThe game is simple. You will be presented with two Twitter users.\n")
print("You will be asked to guess which one has more followers.\n")
print("If you are correct, you will get a point.\n")
print("The game will end when you are wrong.\n")
print("Good luck!\n")

play = True
play = input("Do you want to play? (y/n): ")
if play != 'y':
    print("\nThanks!")
    play = False
while play:
    game()
    screen_clear()
    print(logo)
    play_again = input("\nDo you want to play again? (y/n): ")
    if play_again != 'y':
        print("\nThanks for playing!")
        play = False

