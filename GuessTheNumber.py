# Write a programme where the computer randomly generates a
# number between 0 and 20. The user needs to guess what the number is.
# If the user guesses wrong, tell them their guess is either too high,
# or too low. This will get you started with the random library if
# you haven't already used it.

import random
import time

def guessgame():

    Welcome = ('\nWelcome to "GUESS THE NUMBER" game!\n\nIn this game, the computer will generate a random number from 0 to 20. ' 
            'Guess the generated number by typing your answer on the keyboard.\nYou have 2 chances to win. Shall we start?!\n')
    print(Welcome)
    
    Y = input('Click "Y" to continue\n')
    Y = str(Y)

    if Y == 'Y' or Y == 'y':
        print('\nGenerating number...Patience is a virtue :)\n')

        number = list(range(0, 21))
        number = random.choice(number)
        number = int(number)

        time.sleep(1) #wait 1 second
        guess = input('Done! Please type your guess between 0 and 20.\n')
        guess = int(guess)

        if number > guess:
            print('Generated number is greater than your guess.\n')

        elif number == guess:
            print('Well done! You are correct!\n')
            print('Generated number:' + str(number))
        
        else:
            print("Generated number is lesser than your guess.\n")

    else:
        print('Incorrect command. To continue please type "Y" or "y" on your keyboard.\n')

for i in range(2):
    guessgame()