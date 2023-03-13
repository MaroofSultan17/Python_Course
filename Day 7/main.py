
import random

word_list = ["ardward", "baboon", "sultan"]
chosen_word = random.choice(word_list)
print(f'Chosen word is , {chosen_word}')

display = []
for letter in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a Letter").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("Congratulations :) You WIN")