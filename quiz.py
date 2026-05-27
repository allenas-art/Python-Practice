#Intro
QUESTIONS = 2
print("Hello and welcome to the Dinosaur quiz.")
print(f"We will be using a time machine to go back to the age of dinosaurs and learn all we can through a quiz of {QUESTIONS} questions.")

#Recording users name

name = input("But before I show you the time machine and we head out, I have to know, what is your name?")

#Ascii Art
print(r"       \\=====\\ "                                      )
print(r"        \\      \\  "                                   )                                                                                             
print(r"        \\ {   }  \\  "                                 )                                                                                              
print(r"        \\           \\  "                              )                                                                                              
print(r"         ================   "                           )                                                                                                 
print(r"          \\             \\   "                         )                                                                                   
print(r"           \\             \\   "                        )                                                                                                                                
print(r"            \\     // \\   \\   "                       )                                                                                                                        
print(r"             \\   {{   }}   \\   "                      )                                                                                                                                   
print(r"              \\   {{    }}  \\   "                     )                                                                                                                                    
print(r"               \\   {{   }}   \\   "                    )                                                                                                                                  
print(r"                \\    \\ //    \\   "                   )                                                                                                                                      
print(r"                 \\             \\   "                  )                                                                                                                                       
print(r"                  \\             \\   "                 )                                                                                                                                     
print(r"                   \\=============\\  "                 )                                                                                                                                        
print(r"                    ||              \\   "              )                                                                                                                                     
print(r"                    ||                \\    "           )                                                                                                                                       
print(r"                    ||  VqpqpqpqpqpqV   \\    "         )                                                                                                                                        
print(r"                    || VqpqpqpqqpqpqpqpV  \\    "       )                                                                                                                                         
print(r"                    || VqpqpqpqpqpqpqpqpqV  \\    "     )                                                                                                                                        
print(r"                    ||  VqpqpqpqpqpqpqpqpqpV  \\    "   )                                                                                                                                           
print(r"                        VqpqpqpqpqpqpqpqpqpqV        "  )                                                                                                                                             
print(r"                          VqpqpqpqqpqpqpqpqpqW        " )                                                                                                                                            
print(r"                            WqpqpqpqpqpqpqpqW          ")                                                                                                                                                
print(r"                               WqpqpqpqpqpqV           ")                                                                                                                                                 
print(r"                                 VqpqpqpqpW            ")                                                                                                                    
print(r"                                    WqpqpqW           " )
print(r"                                       WqppW         "  )
print(r"                                           W       "    )

print("No this is not a rocket ship it is a time machine.")

#First Question 

print(f'Now off we go {name} all the way back to the time of the dinosaurs')
a1 = input("To activate the time machine just enter here how many millions of years ago (in numbers) \
that the dinosaurs began their rule of the world (for example type 100 for 100 million years)")

    #Results for correct answers to first question

if int(a1) >= 225 and int(a1) <= 275:
    print("Correct! Wow that was impresive, I'll have to make it harder then.")

    #Second Question if first question is correct

    a21 = input("Now do you know which of the three periods of the Mezosoic era we have arrived in 250 million years in the past?")
    if a21.strip() and a21.lower() == "triassic":
    
        #Results for correct answer to second & first question 

        print("Correct! Nice job that's two in a row.")
    
        #Results for incorrect answer to second question if correct for first question
    else:
        print("Incorrect, the answer was Triassic, then comes the Jurassic, and Cretaceous. Oh well you couldn't get a streak going.")

    #Results for incorrect answer to first question

else:
    print("Incorrect! The answer was 250(million years ago), unfortunate, but that was a hard one I'm sure you'll get it next time")

    #Second Question (if first question is incorrect)

    a22 = input("Okay, we've arrived 250 million years in the past into a time called the Mesozoic Era, the time of the dinosaurs." 
    "The Mesozoic Era is divided into three periods, do you know which came first? a. The Triassic, b. The Cretaceous, c. The Jurassic (Answer with a, b, or c, only!)")

        #Results for correct answer to second question if incorrect for first question

    if a22.strip() and a22.lower() == "a":
        print("Correct! Nice job! made up for the first question.")

        #Results for first incorrect answer to second question if incorrect for first question

    elif a22.strip() and a22.lower() == "b":
        print("Incorrect, the answer was a. The Triassic, then in order it goes The Jurassic, and The Cretaceous")

        #Results for second incorrect answer to second question if incorrect for first question

    elif a22.strip() and a22.lower() == "c":
        print("Incorrect, the answer was a. The Triassic, then in order it goes The Jurassic, and The Cretaceous")

        #Results for n/a answer to second question if incorrect for first question

    else:
        print("That's not even one of the options, I told you to type a letter!")

print("Now we are going to job forward to 150 million years ago in the Jurassic.")
print("Look to the skies and yrg might see something like this:")
print(r"                           <\              _
                            \\          _/{
                     _       \\       _-   -_
                   /{        / `\   _-     - -_
                 _~  =      ( @  \ -        -  -_
               _- -   ~-_   \( =\ \           -  -_
             _~  -       ~_ | 1 :\ \      _-~-_ -  -_
           _-   -          ~  |V: \ \  _-~     ~-_-  -_
        _-~   -            /  | :  \ \            ~-_- -_
     _-~    -   _.._      {   | : _-``               ~- _-_
  _-~   -__..--~    ~-_  {   : \:}
=~__.--~~              ~-_\  :  /
                           \ : /__
                          //`Y'--\\
                         <+       \\
                          \\      WWW
                          MMM.            ")

