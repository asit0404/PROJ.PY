MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 400,
    "coffee": 200
}
profit = 0
def availability(sufficient):
    """returns true if a order can be made or else"""
    for item in sufficient:
        if sufficient[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def coin_resources():
    """returns the total of money collected"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction(money_got,drink_cost):
    """checks if we can afford"""
    if money_got > drink_cost:
        change = round(money_got - drink_cost,2)
        print(f"you have your change here as {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("not enough money buddy refunded....")
        return False

def make_coffee(coffee_name,order_ingredients):
    """deduct the ingredents from the resourses"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your ☕{coffee_name} ")

ASIT_THE_G=True
while ASIT_THE_G:
    ask= input("What would you like? (espresso/latte/cappuccino):").lower()
    if ask == "off":
        ASIT_THE_G = False
    elif ask == "report":
        print("current resources")
        print(f"the milk left {resources['milk']} ml")
        print(f"the coffee left {resources['coffee']} ml")
        print(f"the water left {resources['water']} ml")
        print(f"the money {profit} $")
    else:
        drink = MENU[ask]
        if availability(drink["ingredients"]):
            payment = coin_resources()
            if transaction(payment,drink['cost']):
                make_coffee(ask,drink['ingredients'])






