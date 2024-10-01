from rules import rule
import os
import random
import sys
import art

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def choice():
    choices_list = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices_list)


def result(cmp_ch, us_ch):
    if ((cmp_ch == "Rock") & (us_ch == "Paper")) or ((cmp_ch == "Paper") & (us_ch == "Scissor")) or ((cmp_ch == "Scissor") & (us_ch == "Rock")):
        return "Win"
    if ((cmp_ch == "Rock") & (us_ch == "Scissor")) or ((cmp_ch == "Paper") & (us_ch == "Rock"))or ((cmp_ch == "Scissor") & (us_ch == "Paper")):
        return "Lose"
    if ((cmp_ch == "Rock") & (us_ch == "Rock")) or ((cmp_ch == "Paper") & (us_ch == "Paper")) or ((cmp_ch == "Scissor") & (us_ch == "Scissor")):
        return "Draw"


def get_input():
    try:
        us_ch = int(input("What is your choice [Rock(1) or Paper(2) or Scissor(3)]: ").strip())
    except TypeError:
        sys.exit("Incorrect input")
    if us_ch == 1:
        return "Rock"
    elif us_ch == 2:
        return "Paper"
    elif us_ch == 3:
        return "Scissor"
    else:
        sys.exit("Incorrect input")


def print_choice(choice):
    if choice == "Rock":
        return art.rock
    elif choice == "Paper":
        return art.paper
    elif choice == "Scissor":
        return art.scissor


def game():
    computer_choice = choice()
    user_choice = get_input()

    print(f"Your choice is {user_choice}")
    print(f"The computer's choice is {computer_choice}")
    print(print_choice(user_choice) + vs_logo + print_choice(computer_choice))
    
    if result(computer_choice, user_choice) == "Win":
        print("You Win!")
    elif result(computer_choice, user_choice) == "Draw":
        print("It's a draw.")
    else:
        print("You lose!")


vs_logo = """
 ___      ___  ________  
|"  \    /"  |/"       ) 
 \   \  //  /(:   \___/  
  \\  \/. ./  \___  \    
   \.    //    __/  \\   
    \\   /    /" \   :)  
     \__/    (_______/   
                         
"""


def main():
    while True:
        clear()
        print(art.logo)
        print(rule)
        game()
        if input("Do you wanna play again (y or n): ").lower().strip() == "y":
            continue
        break


if __name__ == "__main__":
    main()