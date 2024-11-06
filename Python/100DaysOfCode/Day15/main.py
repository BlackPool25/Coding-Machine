import sys

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

drinks = ['espresso', 'latte', 'cappuccino']
profit = 0
is_on = True
resources = {
    "water": 300,
    "milk" : 200,
    "coffee" : 100
}

def print_report():
    print(f"Water : {resources["water"]} ml.")
    print(f"Milk: {resources["milk"]} ml.")
    print(f"Coffee: {resources["coffee"]} g.")
    print(f"Profit: ${profit}.")


def is_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]> resources[item]:
            print(f"Insuffient {item}.")
            return False
        print(f"{item} checked.")
    return True


def process_coins():
    total = 0
    total += int(input("Input quarters: ").strip()) * 0.25
    total+= int(input("Input dimes: ").strip()) * 0.1
    total += int(input("Input nickles: ").strip()) * 0.05
    total += int(input("Input pennies: ").strip()) * 0.01
    return total


def transaction_successful(payment, cost):
    if payment>=cost:
        change = round(payment-cost , 2)
        print(f"Here is your change ${change}.")
        profit += cost
        return True
    else:
        print("Sorry not enough money.")
        return False


while is_on:
    choice = input("Enter your choice (espresso/latte/cappuccino): ").strip().lower()

    if choice == "off":
        sys.exit("Thank you.")

    elif choice == "report":
        print_report()

    elif choice in drinks:
        drink = MENU[choice]
        if is_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_drink(drink, drink["ingredients"])