from art_day9 import logo
print(logo)

import os
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      clear = os.system('clear')
   else:
      # for windows platfrom
      clear = os.system('cls')
      
bids = {}
bidding = True
highest_bid = 0
while bidding:
    bidder_name = input("What's your name? ")
    
    bids[bidder_name] = int(input("What's your bid? "))
    
    another = input("anyone else? y for yes or n for no ")
    screen_clear()
    if another.lower() != "y":
        bidding = False
        

for bidder in bids:
    bid = bids[bidder]
    if bid > highest_bid:
        highest_bid = bid
        winner = bidder
    
    
print(f"The winner is {winner} with a bid of ${highest_bid}")
