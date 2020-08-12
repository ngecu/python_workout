
import random
def guessing_game():
    x = random.randint(0, 100)
    while True:
        answer = int(input('What is your guess? '))
        if answer == x:
            print('Correct answer')
            break
        if answer < x:
            print('Too low')
        else:
            print('Too High')

guessing_game()