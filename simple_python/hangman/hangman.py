import random
from hangman_words import word_list
from hangman_art import logo, stages
import os

os.system('clear')


END_OF_GAME = False
lives = 6

# randomly choose a word from word list
choosen_word = random.choice(word_list)
word_length = len(choosen_word)

print(logo)

# Testing Code
print(f'Pssst, the solution is {choosen_word}')


# Create a list with '_' equal to number of characters in choosen word 
display =[]
for _ in  range(len(choosen_word)):
    display += "_"


while not END_OF_GAME:
    guess = input("Guess a letter : ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(len(choosen_word)):
        if choosen_word[position] == guess:
            display[position] = guess

    if  guess not in choosen_word:
        print(f"You Guessed {guess}, that  is not in the word. You loose a life")
        print(stages[lives])
        lives -= 1
        if lives == 0:
            END_OF_GAME = True
            print(stages[0])
            print("You Lose!!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        END_OF_GAME = True
        print(f"You Win!!")



