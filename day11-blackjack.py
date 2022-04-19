from blackjack_art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

Play = input("Would you like to play Blackjack? (y/n) ")

def calculate_score(cards):
    score = 0
    for card in cards:
        score += card
    if score > 21:
        for card in cards:
            if card == 11:
                score -= 10
                if score <= 21:
                    return score
    
    return score

def game(user_score, computer_score):

    if user_score == computer_score:
        print("It's a draw!")
    elif user_score > 21:
        print("You have over 21! You lose!")
    elif computer_score > 21:
        print("The computer has over 21! You win!")
    elif user_score == 21  :
        print("You have a blackjack! You win!")
    elif computer_score == 21 :
        print("The computer has a blackjack! You lose!")
    elif ( user_score>computer_score and user_score<21 ):
        print("You win!")
    elif ( user_score<computer_score and user_score<21 ):
        print("You lose!")
    
    
        
while Play == "y":
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards)) 

    user_score = calculate_score(user_cards)
    

    print(f"You have: {user_cards}"), print(f"Computer's first card: {computer_cards[0]}")
    print(f"Your score is: {user_score}")
    
    more_cards = input("Would you like to draw another card? (y/n) ")
    

    while more_cards == "y":
        user_cards.append(random.choice(cards))
        user_score = calculate_score(user_cards)
        print(f"Your score is: {user_score}")
        more_cards = input("Would you like to draw another card? (y/n) ")

    computer_score = calculate_score(computer_cards)
    
    
    while computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = calculate_score(computer_cards)

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your score is: {user_score}"), print(f"Computer's score is: {computer_score}")

    game(user_score, computer_score) 
    
    Play = input("Would you like to play again? (y/n) ")

print("Thanks for playing!")
print("See you next time!")








