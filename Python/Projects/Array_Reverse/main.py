import os
from art import logo
import sys

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def reverse(string):
    rev_str = ""
    for i in string:
        rev_str = i + rev_str
    return rev_str


def main():
    try:
        clear()
        print(logo)
        user_str = input("Enter a string: ").strip()
        print(f"The reversed string is {reverse(user_str)}.")
        if reverse(user_str) == user_str:
            print("Your string is a palindrome.")
        else:
            pass
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()