#import random
import random

#define function
def guessing_game():
    x = random.randint(0,100)
    while True:
        answer = int(input("what is your guess?"))
        if answer == x:
            print("Correct answer")
            break
        if answer < x:
            print("too low")
        else:
            print("Too High")
        

guessing_game()
