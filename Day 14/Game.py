from Art import logo, vs
from game_data import data
import random
from replit import clear

print(logo)

count = 0
game_shd_cont = True
account_b = random.choice(data)

def format_data(account):
    # formatting data for A
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc}, From {account_country} ."


def chk_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    elif b_followers > a_followers:
        return guess == 'b'


while game_shd_cont:
    clear()
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask from a User
    guess = input("Who has more Followers ? Type 'A' and 'B' : ").lower()
    ans_a = account_a["follower_count"]
    ans_b = account_b["follower_count"]
    is_correct = chk_answer(guess, ans_a, ans_b)

    # give user feedback
    if is_correct:
        count += 1
        print(f"You're Right! Current score is {count}")
    else:
        game_shd_cont = False
        print(f"Sorry Wrong Your score is {count}")
