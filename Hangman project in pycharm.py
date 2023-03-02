import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import hangman_words
list_of_words = hangman_words.word_list
chosen_word = random.choice(list_of_words)
# word is chosen from a hangman_words.py file word list randomly. 

display = []

for letters in chosen_word:
    display.append("_")
# print(f"The word is {chosen_word}.")
print(f"Word consists of {len(display)} letters.")
print(display)
lives = 6
no_of_guess = 0

while True:
    guess = input("Guess a letter: ").lower()
    no_of_guess+=1
    for position in range(len(chosen_word)):
        word = chosen_word[position]
        if word == guess:
            display[position] = word
    print(display)

    if "_" not in display:
        print("You won!!!")
        break
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            print("You lose as you have no lives left.")
            break

    print(stages[lives])
    print(f"You have {lives} lives left.")

print(f"The word is {chosen_word}.")







