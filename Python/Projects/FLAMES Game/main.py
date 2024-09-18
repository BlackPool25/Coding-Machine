# importing files
from Flame_art import art
import os

# taking input from the user
def take_input():
    name1 = input("Player 1 Name: ").upper().strip()
    name2 = input("Player 2 Name: ").upper().strip()
    return name1, name2


# removing characters that are in both names
def trim(n1,n2):
    for character in n1:
        if (character in n2):
            n1 = n1.replace(character, "", 1)
            n2 = n2.replace(character, "", 1)
    return n1,n2


# counting the number of characters
def count_names(n1, n2):
    n1, n2 = trim(n1,n2)
    return len(n1) + len(n2)


# Displaying the result
def result(element):
    match element:
        case "F":
            print("Relationship Status: Friends.")
        case "L":
            print("Relationship Status: Lovers.")
        case "A":
            print("Relationship Status: Affectionate.")
        case "M":
            print("Relationship Status: Marriage.")
        case "E":
            print("Relationship Status: Enemies.")
        case "S":
            print("Relationship Status: Siblings.")


# Clearing the terminal during execution
def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


# The actual Game
def game():
    print(art)
    name1, name2 = take_input()
    count_name = count_names(name1, name2)
    flames = ["F", "L", "A", "M", "E", "S"]
    index = -1 
    while(len(flames) > 1):
        index += count_name
        if index>len(flames)-1:
            index = (index%len(flames))
        flames.remove(flames[index])
        index -= 1
    result(flames[0])


# Main Function
def main():
    while True:
        clear()
        game()
        
        if input("Do you wanna try again (y or n): ").lower().strip() == "y":
            continue
        else:
            break

    
main()