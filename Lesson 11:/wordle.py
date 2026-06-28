# =====================================================================
# PROJECT: Wordle
# Create a program where the user must guess the 5 letter word.
# =====================================================================

# TOOLS
# TODO Import random so you can randomise the word
import random
# VALUES
# TODO Create a list of at least 5 different 5-letter words
# TODO Create a variable called play and set it to True
words = ["trade","irate","pearl","audio","apple"]
# INTRODUCTION
# TODO Tell your user how to play wordle (make sure they know they must input 5 letter words)
print("This is wordle")
play = True
# TODO Create a while loop that runs if play is true
while play == True:
    # TODO Create word variable and store a random word from your list (using random.choice)
    the_word = random.choice(words)
    # USER INPUT
    # TODO Get user's first guess and save it into a variable
    # TODO Create a while loop if the guess is not 5 characters long
        # TODO Tell them it's not 5 letters and to try again
    guess = input("What is your guess ")
    while (len(guess)) != 5:
        print("That is not a five a letter word try again ")
    # TODO Check if they got it correct and if they did, tell them so and then break the loop
    if guess == the_word:
        print("You got it!")
        break
    else:
    # TODO Create a for loop that loops 5 times
        # TODO Check if the current letter of user_input (user_input[i]) is the same as the i letter of the word and if it is tell them they got that letter correct
        for i in range(5):
            if (guess[i]) == (the_word[i]):
                print(f"letter {i+1} is correct")
        # TODO Otherwise check if the current letter of user_input is in the word and if it is, tell them that letter is in the wrong position
            elif (guess[i]) in the_word:
                print(f"Letter {i+1} is in the wrong place")

        # TODO Else tell them that letter is wrong
            else:
                print(f"letter {i+1} is wrong ")
# TODO Ask if they want to play again. If they don't, set play to false.
    playagain = input("Do you want to play again?")

# ==========================================================
# EXTENSION
# Instead of telling the user one by one about their letters, put each correct letter and _ for a wrong letter into a list. 
# Then finally print the list (you can use "".join(list_name) to merge them into a string if you like)

# ==========================================================
# EXPERT
# Following on from the extension, add colour to the letters instead (Don't use _ for incorrect anymore). Green for correct, orange for wrong place, red for incorrect. You'll need to add the colour as you add them to the list

# print("\033[31mThis is Red Text\033[0m")
# print("\033[38;2;255;165;0mThis is Orange Text\033[0m")
# print("\033[32mThis is Green Text\033[0m")

# Further Extension: Structure with user defined functions