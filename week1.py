from random import randint
from IPython.display import clear_output
"""
Week 1 
Focus was to use command line and jupyter notebook (I used pycharm instead) 
"""
guessed = False
number = randint(0,100)
guesses = 0
while not guessed:
    ans = input("Try to guess the number I am thinking of!")
    guesses +=1
    clear_output()
    if int(ans) == number:
        print("Congrats! You guess it correctly")
        print("It took you {} guesses!".format(guesses))
        break
    elif int(ans) > number:
        print("The number is lowered than what you guessed")
    elif int(ans) < number:
        print("The number is greater than what you guessed")
