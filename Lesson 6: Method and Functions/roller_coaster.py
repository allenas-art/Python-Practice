# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Get input
age = input("How old are you?")
if int(age) <= 10: 
    print("You are too young")
else:
    print(" You are old enough")
    height = input(" How tall are you in centimeters?")
    if int(height) <= 150:
        print(" You are not tall enough")
    else:
        print("you are tall enough")
        Condition = input("Do you have a heart condition?")
        if Condition == "yes":
            print("You cannot ride the roller coaster")
        else:
            print("You can ride!!")


# Check conditions and output verdict




# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient