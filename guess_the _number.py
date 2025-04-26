import random
easy_level=10
hard_level=5
from logo_2 import hello
def check_answer(u_guess,actual_answer,turns):
    if u_guess > actual_answer:
        print("too high")
        return turns - 1
    elif u_guess < actual_answer:
        print("too low")
        return turns - 1
    else:
        print(f"you won your answer is {actual_answer}")
        return turns
def difficulty():
    leave = input("choose a difficulty leavel type 'easy' or 'hard'").lower()
    if leave == "easy":
        return easy_level
    else:
        return hard_level

def game():
    input("welcome to the number guessing game, press enter to continue")
    print(hello)
    print("think of a number btw 1 to 100")
    answer= random.randint(1,100)
    turns = difficulty()

    guess = 0
    while guess!=answer:
        print(f"you have {turns} attempts remaining to guess the number")
        guess = int(input("guess a number: "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print(f"you've run out of guesses the answer was {answer}")
            return
game()
