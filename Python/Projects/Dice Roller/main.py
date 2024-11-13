import random
import sys
import os


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    clear()
    try:
        while True:
            print(f"The roll of the dice is : {random.randint(1,6)}")
    
    except KeyboardInterrupt:
        clear()
        sys.exit("Thank you!")


if __name__ == "__main__":
    main()