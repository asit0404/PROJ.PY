import random
from art import logo

def del_card():
    """returns a random card from the deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    """take the list of cards amd return the score of calculated cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return "blackjack"
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, comp_score):
    if u_score == comp_score:
        return "draw"
    elif comp_score == "blackjack":
        return "you lost it : computer won"
    elif u_score == "blackjack":
        return "you won hoorey"
    elif u_score > 21:
        return "you lost"
    elif comp_score > 21:
        return "you won computer lost it"
    elif u_score > comp_score:
        return "you win"
    else:
        return "you lost"
def play_game():
    print(logo)
    user_cards= []
    computer_card=[]
    is_gameover = False
    for _ in range(2):
        user_cards.append(del_card())
        computer_card.append(del_card())
    while not is_gameover:
        user_score=calculate_score(user_cards)
        computer_score = calculate_score(computer_card)
        print(f"user {user_cards} and score is {user_score}.")
        print(f"comp first card is {computer_card} and computer score is {computer_score}")
        if user_score == "blackjack" or computer_score == "blackjack" or user_score > 21:
            is_gameover = True
        else:
            add_of_card=input("type 'y' to addd another card 'n' to pass")
            if add_of_card == "y":
                user_cards.append(del_card())
            else:
                is_gameover = True
    while computer_score !="blackjack" and computer_score < 17:
        computer_card.append(del_card())
        computer_score = calculate_score(computer_card)
        print(f"Computer draws a card: {computer_card[-1]} | New score: {computer_score}")
        print(compare(user_score,computer_score))
while (input("wanna play a game--------- 'hail yeah'")) == "y":
    print("\n" *20)
    play_game()
