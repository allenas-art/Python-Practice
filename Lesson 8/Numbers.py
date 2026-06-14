# =====================================================================
# PROGRAM: Higher or Lower Number Guesser
# =====================================================================

# IMPORTS
# TODO: Import the 'random' module so you can generate a secret number.
import random
# VARIABLES
# TODO: Generate a random number between 1 and 100 and save it to 'secret_number'.
number = random.randint(0,100)
# TODO: Create a variable to keep track of the user's current guess.
guess = 0
#       (Hint: Start it as 0 so it doesn't accidentally match the secret number!)


# INTRODUCE THE GAME
# TODO: Print a welcome message explaining that the number is between 1 and 100.
print("Hello, guess my number")
guess = input("Whats your guess ")
# START THE GAME
# TODO: Start a 'while' loop that keeps running AS LONG AS the 
while int(guess) != int(number):
    if int(guess) < int(number):
        guess = input("Higher, try again ")
    elif int(guess) > int(number):
        guess = input("Lower, try again ")   
print("nice job")
print("You guessed the number!")
# GAME OVER / WINNING MESSAGE
# TODO: Print a big victory message telling them they got it right!

# ===========================================
# EXTENSION
# TODO: Create a play again option (you'll need to loop the whole code, including creating the random number)
# TODO: Add an extra condition that tells them if they are within 5 of the secret number

# ===========================================
# EXPERT
# TODO: Try to structure the program using defined functions
