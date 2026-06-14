# =====================================================================
# Task: Country Guessing Game
# =====================================================================

# VALUES
# TODO: Create a variable to store the correct country (e.g., "Italy").
country = "Malaysia"
# TODO: Create a variable to keep track of the user's current guess. 
guess = ""
#       (Hint: Start it as an empty string "" so the loop runs at least once!)

guess = input("Guess my country ")
while guess != "Malaysia" :
    print("Incorrect") 
    guess = input("Try again")
print("Nice Job")
   