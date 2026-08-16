player_choices_list = []
replay = True

#First choice in the game, pre intro

def choice_one_section(player_choices_list):
    
    choice_one = input("You have a choice between a gun or a bow," 
                        " what will you pick? ")
    
    #Results of the first choice, 
    #looped to make sure the user picks one of two options.                    
                        
    while True:
        if choice_one.lower().strip() in \
        ['gun','g','the gun','a gun','i choose the gun']:
            
            print("You pick the gun and it's ammo, "
                "as well as your trusty pig knife")
            #Adding answer to list, saving it to check later
            player_choices_list.insert(0,choice_one.lower().strip())
            return
        
        elif choice_one.lower().strip() in \
        ['bow','b','the bow','a bow','i choose the bow']:
            
            print("You pick the bow and arrows, \n"
                "as well as your trusty pig knife")
            #Adding answer to list, saving it to check later
            player_choices_list.insert(0,choice_one.lower().strip())
            return
        
        else:
            choice_one = input("You have to type either 'gun' or 'bow' ")
        
#Intro to the game

def intro():
    
    print("You are a pig hunter, bla bla backstory")
    
#Second choice in the game.
    
def choice_two_section(player_choices_list):
    
    print("As you leave your cabin you lick your finger \n" 
          "and raise it to the wind. The breeze travels East")
    choice_two = input("Would you like to follow the breeze East or \n" 
                       "travel against it, going West. ")
                       
    #Results of the second choice, 
    #looped to make sure the user picks one of two options.

    while True:         
        if choice_two.lower().strip() in \
        ['east','i go east','i choose east','go east']:
        
            print("You begin to head East, with the wind on your back.")
            #Adding answer to list, saving it to check later
            player_choices_list.insert(1,choice_two.lower().strip())
            return
    
        elif choice_two.lower().strip() in \
        ['west','i go west','i choose west','go west']:
        
            print("You begin to head West, with the wind on your face.")
            #Adding answer to list, saving it to check later
            player_choices_list.insert(1,choice_two.lower().strip())   
            return
    
        else:
            print("You have to type either 'East', or 'West'.")
    
#Third choice of the game
    
def choice_three_section(player_choices_list,replay):
    
    print("After travelling for ages bla bla"
    "bla you find a boar about 100m away.")
    choice_three = input("You can move closer to in the hopes of a better shot"
    "or you can shoot from where you are standing."
    "Type '1' to move closer and '2' to shoot from where you are")
    
    
    
    while True:
        if choice_three.strip() == "1":
            #Adding answer to list, saving it to check later
            player_choices_list.insert(2,choice_three.lower().strip())
            break
        elif choice_three.strip() == "2":
            #Adding answer to list, saving it to check later
            player_choices_list.insert (2,choice_three.lower().strip())
            break
        else:
            choice_three = input("You must either type '1' to move closer "
            "or '2' to shoot from where you are standing!")
    
    #Results of the third choice, 
    #looped to make sure the user picks one of two options.
    
    if player_choices_list[1] == "east"\
    and player_choices_list[2] == "1":
        print("Your scent is carried towards the boar by the wind." \
        "It quickly smells you and, before you can shoot it sprints towards you." \
        "You quickly react by pulling out your knife and preparing to " \
        "stick it. It's charging at you, everything seems to slow down "\
        "and just as it reaches you, you stab it in the gut." \
        "Before you can celebrate though, you feel a wet sensation on your stomach," \
        "as you fall to the ground you smell blood" )

        ending(replay)

    if player_choices_list[2] == "bow" \
    and player_choices_list[0] == "2":
        print("Your bow doesn't have enough range to make the shot." \
        "The arrow glides through the air and hits just shy of the boar" \
        "You are forced to return home empty handed")
        ending(replay)

    elif player_choices_list[1] == "west" \
    and player_choices_list[2] == "1":
        print("You creep ever closer to the boar, " \
        "and feel as though you could reach out to touch it." \
        "But you resist, and shoot it right through the ear as it eats." \
        "It falls before it could even squeal, and you pick it up" \
        "and carry it home on your back.")
        ending(replay)

    elif player_choices_list[0] == "gun" \
    and player_choices_list[2] == "2":
        print("The bullet zips along with a thunderous bang, " \
        "before your ears can begin to ring you hear a squeal and the boar falls in the distance"\
        "You go to pick up the boar, and carry it home on your back.")
        ending(replay)

def ending(replay):

    replay_true_false = input("Game Over, Would you like to play again?")

    while True:
        
        if replay_true_false.lower().strip() in ["yes","true","sure","yeah"]:
            return
        elif replay_true_false.lower().strip() in ["no","false","no way","nah"]:
            print("shutting down") 
            replay = "false"
            return False
        else:
            replay_true_false = input("You must type yes or no")



while True:
    choice_one_section(player_choices_list)
    choice_two_section(player_choices_list)
    choice_three_section(player_choices_list, replay)
    