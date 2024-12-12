import random
game_name=["rock","paper","scissors"]
choose=int(input("what do you choose ? type 0 for ROCK, 1for PAPER, or 2 for SCISSORS : \n"))
if choose>=0 and choose<=2:
    print(game_name[choose])
print(f"you chose {choose}")
a=random.randint(0,2)
print(f"computer chose  {a}")
if choose == 0 and a == 2:
    print("you won")
elif a == 0 and choose == 2:
    print("you lost")
elif choose >= 3 or choose < 0:
    print("invalid")
elif a>choose:
    print("you lost")
elif choose>a:
    print("you won")
elif a == choose:
    print("its a draw")
