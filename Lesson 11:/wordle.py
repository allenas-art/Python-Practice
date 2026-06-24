import random


words = ["apple","rhyme","pearl","audio","trade"]

print("This is wordle")

while True:
   
    the_word=random.choice(words)

    guess = input(" What is your guess? ")   

    if (len(guess)) != 5:
            print("It has to be a five letter word!")
            
    if guess == the_word:
        print("You got it!")
        break
       
    
  
    for i in range(5):
        
        if (guess[i]) == (the_word[i]):
            print(f"Letter {i+1} is correct")
       
        elif (guess[i]) in (the_word[i]):
            print(f"Letter {i+1} is in the word")
       
        else :
            print(f"Letter {i+1} is wrong")


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