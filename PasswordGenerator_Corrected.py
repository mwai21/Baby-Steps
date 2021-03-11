#Challenge 1: Password Generator - 03/Jan
# Write a programme, which generates a random password for the user. 
# Ask the user how long they want their password to be, and how many letters 
# and numbers they want in their password. Have a mix of upper and 
# lowercase letters, as well as numbers and symbols. The password should be 
# a minimum of 6 characters long.

import random
from random import sample
import string


Letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Numbers = '0123456789'
Symbols = '!@#$%^&*'

Password_Lenght = True

def passgenerator():

    Password_Lenght = input('How long would you like your password to be? The password should be a minimum of 6 characters long.\n') #user input to determine password lenght
    Password_Lenght = int(Password_Lenght)

    if Password_Lenght >= 6:
        Number_of_Letters = input('\nHow many letters in the password?\n') #user input to determine quantity of letters
        Number_of_Letters = int(Number_of_Letters)

        quant_numbers = input('\nHow many numbers in the password?\n') #user input to determine quantity of numbers
        quant_numbers = int(quant_numbers)

        password = '' #variable establishes password with empty value

        for i in range(Password_Lenght): #loop and random sample function that will chose from an amount from a list
            step1 = random.sample(Letters, Number_of_Letters) 
            step2 = random.sample(Numbers, quant_numbers)
            step3 = random.sample(Symbols, (Password_Lenght - (Number_of_Letters + quant_numbers)))

            password = ''.join(step1 + step2 + step3) #changes a list to string

            print('Your password is' + password + '\n')

            print('\n' + "Thank you for using our program. See you soon!") #thank you and bye to user

            exit(0) # Exit the program
    
    else:
        print('ERROR:The password should be a minimum of 6 characters long. Please try again.\n') #error message
    
while Password_Lenght: #while loop until input lenght from user is >=6
    passgenerator()


