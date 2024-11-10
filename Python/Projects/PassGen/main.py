import string
import sys
import random


def create(chars):
    return random.choice(chars)


def main():
    try:
        size = int(input("Enter the size: "))
    except ValueError:
        sys.exit("Invalid input.")
    
    password = ""
    all_char = string.ascii_letters + string.digits + string.punctuation
    for _ in range(size):
        password += create(all_char)
    
    print(f"Your password is: {password}")


if __name__ == "__main__":
    main()