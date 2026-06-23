# =====================================================================
# PROJECT: The Magic 8-Ball Fortune Teller
# Create a program that gives random responses to yes/no questions
# =====================================================================


import random

eight = ["It is certain","As I see it, yes","Reply hazy", "try again","Don't count on it", "Without a doubt", "Outlook good","Concentrate and ask again","My sources say no", ]

while True:
    question = input("Ask a yes or no question or type quit to leave ")
    if question == "quit":
        print("goodbye")
        continue
    random_index = random.randint(0,8)
    chosen_fortune = eight[random_index]
    print(f"{chosen_fortune}")
    print("goodbye")
    break

