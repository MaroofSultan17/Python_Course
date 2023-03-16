from random import randint
answer = randint(1, 100)
# Create a function that is check the input number status


def number_chk(predict, user_input):
    if user_input > predict:
        return f"Too High {user_input}"
    elif user_input < predict:
        return f"Too Low {user_input}"
    elif user_input == predict:
        return f"You got it. Answer is {predict}, and you guess {user_input}"
# create a function for easy level


def easy():
    easy_iterate = 10
    while easy_iterate > 0:
        print(f"You have {easy_iterate} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        print(number_chk(answer, guess))
        easy_iterate -= 1
        while guess != answer:
            print("Make again.")
            break
        if guess == answer:
            break
# Create a function for hard level


def hard():
    hard_iterate = 5
    while hard_iterate > 0:
        print(f"You have {hard_iterate} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        print(number_chk(answer, guess))
        hard_iterate -= 1
        while guess != answer:
            print("Make again.")
            break
        if guess == answer:
            break
# Create a function to combine all the code with in a single function


def game():
    print("Welcome ti the Number Guessing game!")
    print("i'm Thinking of a number between 1 and 100.")
    difficulty_level = input("Chose a difficulty. Type 'easy' or 'hard':").lower()
    if difficulty_level == "easy":
        print(f"cheating (Predicting number is {answer}).")
        easy()
    elif difficulty_level == "hard":
        print(f"cheating (Predicting number is {answer}).")
        hard()


# Calling the all program
game()
