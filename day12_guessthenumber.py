from day12_art import logo
print(logo)

import random
from random import randint


def guess_the_number():
    difficulty = input("Choose a difficulty level (1-3): ")
    if difficulty == "1":
        chances = 10
    elif difficulty == "2":
        chances = 5
    elif difficulty == "3":
        chances = 3

    answer = random.randint(1, 100)
    while chances>0:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess == answer:
                print("You guessed it!")
                break
            elif guess > answer + 10:
                print("Too high! Try a smaller number!")
                chances -= 1
            elif guess > answer :
                print("A bit high! Try a smaller number!")
                chances -= 1
            elif guess < answer - 10:
                print("Too low! Try a larger number!")
                chances -= 1
            elif guess < answer :
                print("A bit low! Try a larger number!")
                chances -= 1
        except ValueError:
            print("That's not a number! Try typing a number.")   
        if chances == 0:
            print("You ran out of chances! The answer was", answer)
            print("Game over!")
game = True
while game:
    guess_the_number()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again != "y":
        game = False
        print("Thanks for playing!")
        


    



