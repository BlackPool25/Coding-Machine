from art import hand_1,hand_2
import time
import os
import platform
import sys

def cls():
    if platform.system()=="Windows":
        os.system('cls')
    else:
        os.system('clear')


def main():
    try:
        while True:
            print(hand_1, end=cls())
            time.sleep(0.5)
            print(hand_2, end=cls())
            time.sleep(0.5)
    except KeyboardInterrupt:
        cls()
        sys.exit()


if __name__=="__main__":
    main()   
