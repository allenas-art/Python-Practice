

QUESTIONS = 5
score = 0

#answer dictionary

answers = {"q1_a1": 225, "q1_a2": 275, "q2_1": "triassic", "q3_a1": "f", "q3_a2": "false", "q4": "b", "q5": "c"}


def get_name():

    
        #Recording users name
        
    name = input("But before I show you the time machine and we head out, I have to know, what is your name? ")

    return name

def intro():

    #intro

    print("Hello and welcome to the Dinosaur quiz.")
    print(f"We will be using a time machine to go back to the age of dinosaurs" 
          f" and learn all we can through a quiz of {QUESTIONS} questions.")


def intro2():

    #intro for second playthrough

    print("Hello again and welcome to the Dinosaur quiz.")
    print(f"As you know we will be using a time machine to go back to the age of dinosaurs" 
          f" and learn all we can through a quiz of {QUESTIONS} questions.")
    input("Are you ready? ")
    

def question_1(name):

    global score

       #Ascii Art
    print(r"       \\=====\\ " )                                     
    print(r"        \\      \\  ")                                   
    print(r"        \\ {   }  \\  ")                                 
    print(r"        \\           \\  ")                              
    print(r"         ================   ")                           
    print(r"          \\             \\   ")                         
    print(r"           \\             \\   ")                          
    print(r"            \\     // \\   \\   ")                       
    print(r"             \\   {{   }}   \\   ")                      
    print(r"              \\   {{    }}  \\   ")                    
    print(r"               \\   {{   }}   \\   ")                    
    print(r"                \\    \\ //    \\   ")                   
    print(r"                 \\             \\   ")                  
    print(r"                  \\             \\   ")                 
    print(r"                   \\=============\\   ")                 
    print(r"                    ||              \\   ")              
    print(r"                    ||                \\    ")           
    print(r"                    ||  VqpqpqpqpqpqV   \\    ")         
    print(r"                    || VqpqpqpqqpqpqpqpV  \\    ")       
    print(r"                    || VqpqpqpqpqpqpqpqpqV  \\    ")     
    print(r"                    ||  VqpqpqpqpqpqpqpqpqpV  \\    ")   
    print(r"                        VqpqpqpqpqpqpqpqpqpqV        ")  
    print(r"                          VqpqpqpqqpqpqpqpqpqW        ") 
    print(r"                            WqpqpqpqpqpqpqpqW          ")
    print(r"                               WqpqpqpqpqpqV           ")
    print(r"                                 VqpqpqpqpW            ")
    print(r"                                    WqpqpqW           ") 
    print(r"                                       WqppW         ")  
    print(r"                                           W       ")    

    print("No this is not a rocket ship it is a time machine.")

    #First Question

    print(f'Now off we go {name} all the way back to the time of the dinosaurs')

    a1 = input("To activate the time machine just enter here how many millions of years ago (in numbers) \n"
        "that the dinosaurs began their rule of the world (for example type 100 for 100 million years) ")

    while True:
        try:
            a1 = int(a1)
            break
        except:
            a1 = input("\n" 
            "That's not a number try again ")

    #Results for correct answers to first question
  
    if int(a1) >= answers["q1_a1"] and int(a1) <= answers["q1_a2"]:
        print("\n"
              "Correct! Wow that was impressive, I'll have to make it harder then.")
        score += 1
        question_2_1()

    #Results for incorrect answer to first question

    else:
        print("\n"
              "Incorrect! The answer was 250(million years ago), unfortunate, but that was a hard one I'm sure you'll get it next time")
        question_2_2()

def question_2_1():

    global score

    #Second Question if first question is correct

    a21 = input("Now do you know which of the three periods of the Mezosoic era we have arrived in 250 million years in the past? ")
    if a21.strip().lower() == answers["q2_1"] :

        #Results for correct answer to second & first question

        print("\n"
              "Correct! Nice job that's two in a row.")
        score += 1

        #Results for incorrect answer to second question if correct for first question

    else:
        print("\n"
              "Incorrect, the answer was Triassic, then comes the Jurassic, and Cretaceous. Oh well you couldn't get a streak going.")

def question_2_2():

    global score

    #Second Question (if first question is incorrect)

    a22 = input("\n"
                "Okay, we've arrived 250 million years in the past into a time called the Mesozoic Era, the time of the dinosaurs. \n"
    "The Mesozoic Era is divided into three periods, do you know which came first? \n"
        "a. The Triassic, \n"
        "b. The Cretaceous, \n "
        "c. The Jurassic \n "
        "(Answer with a, b, or c, only!)\n ")
    
    #Results for n/a answer to second question if incorrect for first question

    while True:
        if a22.strip().lower() in ["a","b","c"]:
            break
        else:
            a22 = input("\n"
                        "That's not even one of the options, I told you to type a letter! I'll give you one more try. Do you know which came first? \n"
            "a. The Triassic, \n"
            "b. The Cretaceous, \n"
            "c. The Jurassic \n"
            "(Answer with a, b, or c, only!) \n")
        

    #Results for correct answer to second question while incorrect for first question

    if a22.strip().lower() == "a":
        print("\n"
              "Correct! Nice job! made up for the first question.")
        score += 1
    #Results for first incorrect answer to second question while incorrect for first question

    elif a22.strip().lower() == "b":
        print("\n"
              "Incorrect, the answer was a. The Triassic, then in order it goes The Jurassic, and The Cretaceous")

    #Results for second incorrect answer to second question if incorrect for first question

    elif a22.strip().lower() == "c":
        print("\n"
              "Incorrect, the answer was a. The Triassic, then in order it goes The Jurassic, and The Cretaceous")



def question_3():

    global score

    #Question 3

    input("Are you ready for question 3? ")
    print("Now we are going to jump forward to 150 million years ago in the Jurassic.")
    print("Look to the skies and you might see something like this:")
    print(r"                             <\             _                   " )
    print(r"                              \\          _/{                   " )
    print(r"                       _       \\       _-   -_                 ")
    print(r"                     /{        / `\   _-     - -_               ")
    print(r"                   _~  =      ( @  \ -        -  -_             ")
    print(r"                 _- -   ~-_   \( =\ \           -  -_           ")
    print(r"               _~  -       ~_ | 1 :\ \      _-~-_ -  -_         ")
    print(r"             _-   -          ~  |V: \ \  _-~     ~-_-  -_       ")
    print(r"          _-~   -            /  | :  \ \            ~-_- -_     ")
    print(r"       _-~    -   _.._      {   | : _-``               ~- _-_   ")
    print(r"    _-~   -__..--~    ~-_  {   : \:}                            ")
    print(r"  =~__.--~~              ~-_\  :  /                             ")
    print(r"                             \ : /__                            ")
    print(r"                            //`Y'--\\                           ")
    print(r"                          <+       \\                           ")
    print(r"                           \\      WWW                          ")
    print(r"                            MMM                                 ")

    print("This is called a Pterasaur and is one earliest creatures to develop flight (not counting bugs)")
    a3=input("True or False, Pterasaurs are also called Avian-Dinosaurs (Dinosaurs that can fly) ")

    #Results for n/a answer to question 3

    while True:
        if a3.strip().lower() in ["f", "t", "true", "false"]:
            break
        else:
            print("\n" 
                  "You have to answer true or false!")
            a3 = input("True or False, Pterasaurs are also called Avian-Dinosaurs (Dinosaurs that can fly) ")

            
    #Results for correct answer to question 3
    
    if a3.strip().lower() == answers["q3_a1"] or a3.strip().lower() == answers["q3_a2"]:
        print("\n"
              "Correct! well done. Even though Pterasurs and Dinosaurs lived at the same time they are different things altogether. \n" 
        "They share a common ancester but evolved differently.")
        score += 1

    #Results for incorrect answer to question 3

    elif a3.strip().lower() == "t" or a3.strip().lower() == "true":
        print("\n"
              "Incorrect! Even though Pterasurs and Dinosaurs lived at the same time they are different things altogether. They share a common ancester but evolved differently.")

    


def question_4():

    global score

    #Question 4

    a4 = input("\n"
               "Next question, what is the name of the tail of a Stegosaurus. \n"
        "a. Segamiser \n"
        "b. Thagomizer \n"
        "c. Gominizer \n")
    
    #Question 4 n/a answer    
     
    while True:
        if a4.strip().lower() in ["a","b","c",]:
            break
        else:
            a4 = input("\n"
                       "That's not one of the answers. it has to be a. b. or c. ")

    #Question 4 correct answer

    if a4.strip().lower() == answers["q4"]:
        print("\n"
              "Nice job thats correct!")
        score += 1

    #Question 4 incorrect answer
    elif a4.strip().lower() in ["a", "c"]:
        print("\n"
              "Incorrect, the answer was b. Thagomizer")

    
def question_5():

    global score

    #Question 5

    a5 = input("\n"
               "The final question, and the hardest one yet, I'd be impressed if you got it. \n"
            "What period did the Baryonyx live \n"
            "a. Triassic \n"
            "b. Jurassic \n"
            "c. Cretaceous \n")
    
    #Question 5 n/a answer    

    
     
    while True:
        if a5.strip().lower() in ["a","b","c",]:
            break
        else:
            a5 = input("\n"
                       "That's not one of the answers. it has to be a. b. or c. ")

    #Question 5 correct answer

    if a5.strip().lower() == answers["q5"]:
        print("\n"
              "Nice job thats correct!")
        score += 1

    #Question 4 incorrect answer
    elif a5.strip().lower() in ["a", "b"]:
        print("\n"
              "Incorrect, the answer was c. Cretaceous")


def outro(name):

    #Ending

    print(f"\n"
          f"Congratulations {name}, you finished the dinosaur quiz! Your score was {score}/{QUESTIONS}")
    replay = input("Would you like to play again? ")
    if replay in ["y", "yes", "yeah", "yup"]:
        return True
    else :
        return False
    
#Execution


intro()
user_name = get_name()


question_1(user_name)


question_3()  
question_4()
question_5()

play_again = outro(user_name)

while play_again == True:
    
    score = 0

    intro2()

    question_1(user_name)

    question_3()

    question_4()

    question_5()

    play_again = outro(user_name)