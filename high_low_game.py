import random
from logo_day_14 import logo, vs
from gamedata import data
print(logo)
score = 0
def calculate(u_score, followers_a, followers_b):
    """thsi calculates weather  a is correct or b"""
    if followers_a > followers_b:
        return u_score == "a"
    else:
        return u_score == "b"
def credentials(value):
    """thsi reyturns the printable outputs of the dictionary"""
    account_name = value['name']
    account_description = value['description']
    account_country = value['country']
    return f"{account_name}, a {account_description}, from {account_country}"
value_2 = random.choice(data)
asit = True
while asit:
    value_1 = value_2
    value_2 = random.choice(data)
    a_followers = value_1['follower_count']
    b_followers = value_2['follower_count']
    if value_1 == value_2:
        value_2 = random.choice(data)
    print(f"compare A: {credentials(value_1)}")
    print(vs)
    print(f"against B: {credentials(value_2)}")
    guess = input("who has more followers 'A' or 'B'").lower()
    output = calculate(guess, a_followers, b_followers)
    if output:
        score += 1
        print("\n" *20)
        print(f"you are correct correct score {score}")
    else:
        print(f"try luck next time final score {score}")
        asit = False


