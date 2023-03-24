'''
POSSIBLE UPDATES:

1. Add multiple lists of words, different categories, and let player choose from
the categories.

2. Create a smart difficulty system, where the max number of guesses changes
depending on the length of the word.

3. Add a "guess the word" option - player can guess the whole word if they know
it, and if they get it wrong they lose instantly.

'''

import random

# list of words to randomly choose from
words = ["python", "java", "ruby", "javascript", "php", "csharp", "swift", "rust"]

# select random word from the list
word = random.choice(words)

# list to keep track of letters guessed
guessedLetters = []

# keep count of number of incorrect guesses
incorrectGuesses = 0


# constant to set maximum number of guesses
MAX_GUESSES = 6

# list of underscore to represent the hidden word
hiddenWord = ["_"] * len(word)


# function to display the state of the game
def showGamestate():
    print(" ".join(hiddenWord))
    print("Guessed letters:", " ".join(guessedLetters))
    print("Incorrect guesses:", incorrectGuesses)
    print("")

# loop until either:
# - player guesses the word
# - player runs out of guesses


while "_" in hiddenWord and incorrectGuesses < MAX_GUESSES:

    showGamestate()

    # get player's guess, and convert to lowercase
    guess = input("Guess a letter: ").lower()

    # check if the letter has already been guessed
    if guess in guessedLetters:
        print("You've already guessed that letter! Try again.")

    # check if the guess is in the word
    elif guess in word:
        print("Correct!")

        # update the hidden word with the correct guess
        for i in range(len(word)):
            if word[i] == guess:
                hiddenWord[i] = guess.upper()

    # if the letter is not in the word, increment incorrectGuesses variable
    else:
        incorrectGuesses += 1

    guessedLetters.append(guess.upper())

# display final state of the game
showGamestate()

# check if player won or lost
if "_" not in hiddenWord:
    print("Congratulations, you guessed the word!")
else:
    print("Sorry, you ran out of guesses. The word was", word)

