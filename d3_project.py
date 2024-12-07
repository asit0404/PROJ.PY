print("WELCOME TO THE TREASSURE HUNT")
choice_1=input('where do you wanna go "left" or "right"\n').lower()
if(choice_1 == "left"):
    choice_2=input('do you want to "swim" or "wait"\n').lower()
    if (choice_2 == "swim"):
        choice_3 = input('what soor would you like to go one "RED"or'
                         ' "blue" or "yellow"\n').lower()
        if (choice_3 == "yellow"):
            print("gameover")
        elif (choice_3 == "red"):
            print("you won meow meow")
        elif (choice_3 == "blue"):
            print("game over")
    else:
        print("game over")
else:
    print("game over")