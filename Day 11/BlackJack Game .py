import random

"""Hint 4: Create a deal_card() function that uses the List below to *return* a random card. 11 is the Ace."""


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


"""Hint 6: Create a function called calculate_score() that takes a List of cards as input and returns the score.
    Look up the sum() function to help you do this. """


def cal_score(cards):
    """Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
     and return 0 instead of the actual score. 0 will represent a blackjack in our game."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    """Hint 8: Inside calculate_score() check for an 11 (ace). 
    If the score is already over 21, remove the 11 and replace it with a 1. 
    You might need to look up append() and remove()."""

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


"""Hint 5: Deal the user and computer 2 
    cards each using deal_card() and append()."""
user_card = []
computer_card = []
for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())
"""Hint 11: The score will need to be rechecked with every new card drawn and the checks in 
Hint 9 need to be repeated until the game ends."""
is_game_over = False
while not is_game_over:
    """Hint 9: Call calculate_score().
     If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends."""
    user_score = cal_score(user_card)
    computer_score = cal_score(computer_card)
    print(f"    Your cards {user_card} and your score is {user_score}")
    print(f"    computer first card is {computer_card[0]}")
    if computer_score == 0 or user_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card and 'n' to pass: ")
        if user_should_deal == 'y':
            user_card.append(deal_card())
        else:
            is_game_over = True

"""Hint 12: Once the user is done, it's time to let the computer play.
 The computer should keep drawing cards as long as it has a score less than 17."""
while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = cal_score(computer_card)

"""Hint 13: Create a function called compare() and pass in the user_score and computer_score. 
 If the computer and user both have the same score, then it's a draw. 
 If the computer has a blackjack (0), then the user loses. 
 If the user has a blackjack (0), then the user wins.
 If the user_score is over 21, then the user loses.
 If the computer_score is over 21, then the computer loses. 
 If none of the above, then the player with the highest score wins."""


def compare(user_score_in, computer_score_in):
    if user_score_in == computer_score_in:
        return "Draw"
    elif computer_score_in == 0:
        return "Lose, opponent has blackjack"
    elif user_score_in == 0:
        return "Congratulations You Win"
    elif user_score_in > 21:
        return "Oh your score is over. YOU LOSE"
    elif computer_score_in > 21:
        return "Oh Computer score is over. COMPUTER LOSE"
    elif user_score_in > computer_score_in:
        return "You Win"
    else:
        return "You Lose"


print(f"    Your final hand {user_card}, Final score : {user_score}")
print(f"    Computer's final Hand {computer_card}, Final score : {computer_score}")
print(compare(user_score, computer_score))
