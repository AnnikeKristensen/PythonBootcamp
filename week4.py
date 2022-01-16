"""Lists and loops
Project: creating hangman"""

from random import choice
from IPython.display import clear_output

# declaring game variables
words = ["tree", "basket", "chair", "paper", "python"]
word = choice(words)
guessed,lives,gameover = [],7,False
guesses = ["_ "]*len(word)

#Init game
while not gameover:
    hidden_word = "".join(guesses)
    print("Guessed letters: {}".format(guessed))
    print("Word to guess: {}".format(hidden_word))
    print("Lives: {}".format(lives))

    answer = input("Type quit or guess a letter: ".lower())
    clear_output()

    #If player types quit
    if answer  == "quit":
        print("Thanks for playing :)")
        gameover == True

    #If player types a letter that has not previously been guessed
    elif answer in word and answer not in guessed:
        print("Yup! That was a correct letter :) ")
        for i in range(len(word)):
            if word[i] == answer:
                guesses[i] = answer
    #If player types a letter they have previously guessed
    elif answer in guessed:
        print("You already guess that.. ")

    #If a player types a letter they havent guessed before but isnt correct
    else:
        lives -= 1
        print("Nope! You got {} lives left".format(lives))

    #Put the letter in the list guessed no matter if its right or wrong
    if answer not in guessed:
        guessed.append(answer)

    #losing
    if lives <= 0:
        print("Oh no, you lost!")
        print("The word was {}".format(word))

    #winning
    elif word == ''.join(guesses):
        print("You guessed correctly!")
        gameover = True

