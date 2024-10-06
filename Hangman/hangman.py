import random
from words import words
import string

def get_valid_words(words):

  word = random.choice(words)
  while '-' in word or ' ' in word:
    word = random.choice(words)
  return word.upper()


def hangman():

  word = get_valid_words(words) # fetch a valid word form the list of words.
  word_letters = set(word) # to track the letter in the random word.
  alpha = set(string.ascii_uppercase) # To get all the uppercase letter in english alphabet.
  used_letters = set() # To get all the alphabet guessed by the user.

  lives = 6

  while len(word_letters) > 0 and lives > 0:
    print("You have used the following letters - ", ' '.join(used_letters))

    word_list = [letter if letter in used_letters else '-' for letter in word]
    print("Current word is: ", ' '.join(word_list))

    user_letter = input("Guess a letter: ").upper()

    if user_letter in alpha - used_letters: # Check if the user has already guessed the letter or not ?
      used_letters.add(user_letter) # Add in the used letter set if already used.
      if user_letter in word_letters: # Checking if the guessed letter is in the letters of the word or not.
        word_letters.remove(user_letter) # Removing the letter from letter of the word set 
      else:
        lives = lives - 1
        print(f" Sorry the letter was not in word, remaining life are {lives}")

    elif user_letter in used_letters: # Checking if the user letter is already used or not ?
      print("Hey, you just guessed that. Try again please ")
    else: # Handle unexpected letters.
      print("Hey that's a invalid character. Please try again. ")

  if(lives == 0):
      print("You died sorry, the word was : ", word)
  else:
      print("You guessed the word correctly: ", word)  
    

hangman()

