import art
import os
from random import randint
from sys import exit

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def game():
    clear()
    print(art.logo)
    guess_num = randint(1,100)
    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
        except TypeError:
            exit("Incorrect input.")
        if user_guess < guess_num:
            print(art.higher)
        if user_guess > guess_num:
            print(art.lower)
        if user_guess == guess_num:
            print(f"You win! The number was {guess_num}.")
            print(art.congrats)
            break
        

def main():
    try:
        while True:
            game()
            if input("Do you wanna play again (y or n)") == "y":
                continue
            print("\nThank you for playing!")
            break
    except KeyboardInterrupt:
        exit("\nThank you for playing!")


if __name__ == "__main__":
    main()