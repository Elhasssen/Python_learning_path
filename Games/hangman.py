import random
from Words import words
import string



def get_valid_world(words):
    word = random.choice(words)  #choose a word randomly from the list words!!! 
    while '-' in word or '' in word: 
        word = random.choice(words)

        return word.upper()

def hangman():
    word = get_valid_world(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed 
    lives = 6
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ''.join(['a','b','cd']) -----> 'a b cd'
        print('you have ', lives, 'lives left and You have used these letters : ', ''.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ''.join(word_list))

        user_letter = input('Guess a letter : ').upper()
        if user_letter in alphabet - used_letters: 
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else: 
                lives = lives - 1
                print('letter is not in word.')
        elif user_letter in used_letters:
            print('the letter is used before, please try again.')
        else:
            print('invalid character, please try again!!')
    if lives == 0:
        print('you died, sorry, the word was', word)
    else:
        print('you guessed the word',word,'!!!!')

hangman()