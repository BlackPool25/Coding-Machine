#Step 5
import os
import random
from hangman_words import *
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]


def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

clear()
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages
print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    print("_ ", end = "")
    display += "_"

print()
    


while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    clear()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    if guess in display:
        print(f"You have already guessed {guess}")

    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    
        
            
    #Check if user is wrong.
    
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        if guess not in chosen_word:
            lives -= 1
            print(f"{guess} is not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
    