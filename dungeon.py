hero_stats = {
    "Name" : "hero", #key : value (name -> key) : (hero -> value)
    "Strength" : 7,
    "Health" : 100.0,
}


def quit ():
    print ("You Chose to Flee\n")
    print ("GAME OVER!")
    return False

def player_stats (): 
    for key, value in hero_stats.items():
        print(f"{key} : {value}" )

def player_move():
    pass

def player_attack():
    pass 


isPlaying = True;

hero_stats["Name"] = input ("What is your name?\n")

player_stats()

while (isPlaying):



    action = input("\nSelect Action: Attack, Move & Flee\n").lower()

    print(f"Player Action: {action}")

    #The above code is an f string LOOK UP DOCUMENTATION FOR THIS 

    if (action == "flee"):
        isPlaying = quit() #<-- isPlaying = False 

    elif (action == "attack"):
        player_attack()
    elif (action == "move"):
        player_move()
    else: 
        print (f"{action} is an invalid action")


  