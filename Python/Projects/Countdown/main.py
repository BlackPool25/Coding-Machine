import time
import sys
import os

def take_input():
    try:
        return int(input("Enter time in seconds: "))
    except TypeError:
        sys.exit("Incorrect type entered")
    

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def timer_func():
    usr_time = take_input()
    while usr_time:
        mins = int(usr_time/60)
        secs = int(usr_time%60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end = "\r")
        time.sleep(1)
        usr_time -= 1
    print("Fire in the hole!!")


def main():
    clear()
    timer_func()


if __name__ == "__main__":
    main()