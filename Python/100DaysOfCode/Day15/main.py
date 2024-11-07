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

# Print the report of ingredients
def print_report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Profit: ${profit}")

# Check if resources are sufficient for the order
def is_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Insufficient {item}.")
            return False
    return True

# Take and return the money received
def process_coins():
    total = 0
    total += int(input("Input quarters: ").strip()) * 0.25
    total += int(input("Input dimes: ").strip()) * 0.1
    total += int(input("Input nickels: ").strip()) * 0.05
    total += int(input("Input pennies: ").strip()) * 0.01
    return total

# Check if payment is sufficient and return change
def transaction_successful(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, not enough money.")
        return False

# Make the drink
def make_drink(drink_name, drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Enjoy your {drink_name}!\n")

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

is_on = True

while is_on:
    for drink in MENU:
        print(f"{drink} costs ${MENU[drink]['cost']}.")
    choice = input("Enter your choice: ").strip().lower()

    if choice == "off":
        is_on = False
        print("Thank you.")
    elif choice == "report":
        print_report()
    elif choice in MENU:
        drink = MENU[choice]
        if is_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])
