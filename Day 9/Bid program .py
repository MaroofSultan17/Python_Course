from replit import clear
from art import logo

print(logo)

bids = {}

bidding_finished = False


def highest_bids(bids_record):
    highest_bid = 0
    winner = ""
    for this in bids_record:
        big_amount = bids_record[this]
        if big_amount > highest_bid:
            highest_bid = big_amount
        winner = this
    print(f"Winner is {winner} with a highest bid $ {highest_bid}")


while not bidding_finished:
    name = input("Please enter your name : ")
    price = int(input("Enter the price "))
    bids[name] = price
    should_finish = input("If anyone more bids then type 'yes' or 'no' \n").lower()
    if should_finish == "no":
        bidding_finished = True
        highest_bids(bids)
    elif should_finish == "yes":
        clear()
