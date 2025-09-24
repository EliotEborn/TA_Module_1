#Assign hero variables for health, attack moves, the damage of the attacks and the inventory
#Track monsters and their health (goblin 30, dragon 200)
# Display hero and master stats at the start
#Allow for ins and functions for attacking and using an item
# Create a graphical grid representation for the game wolrd, player position needs to be indicated and the player needs to be able to move 


hero_stats = {
    "name" : "hero", #key : value (name -> key) : (hero -> value)
    "strength" : 7,
    "health" : 100.0,
}

hero_max_health = 100

health_potion_strength = 5
hero_inventory = ["sword", "health potion", "rope"]

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

def player_heal(item_name):

    if (hero_inventory.count("health potion") <= 0):
        print (f"You don't have any {item_name}")
        return


    hero_stats ["health"] = hero_stats["health"] + health_potion_strength

    if (hero_stats["health"] >= hero_max_health):
        print ("You've at Max health you don't need a health potion!")
        hero_stats["health"] = hero_max_health

    else:
        hero_inventory.remove("health potion")

        print(f"You have used a {item_name}, your health is now {hero_stats['health']}")

        print(f"Your inventory is now {hero_inventory}")

def use_item(): 
    item_name = input(f"What item do you want to use? {hero_inventory}\n")
    print (f"The item you want to use is {item_name}")
    match item_name:

        case "sword":
            pass 

        case "health potion":
            player_heal(item_name)

        case "rope":
            pass 

        case _: 
            print(f"{item_name} is not in your inventory")

#Temporary Function

def damage_player(): 
    hero_stats["health"] = hero_stats["health"] - 10
    print(f"Your Health is now {hero_stats['health']}")


isPlaying = True;

hero_stats["Name"] = input ("What is your name?\n")

player_stats()

while (isPlaying):

    action = input("\nSelect Action: Attack, Use, Move & Flee\n").lower()

    print(f"Player Action: {action}")

    #The above code is an f string LOOK UP DOCUMENTATION FOR THIS 

    if (action == "flee"):
        isPlaying = quit() #<-- isPlaying = False 

    elif (action == "attack"):
        #player_attack()
        damage_player()
    elif (action == "use"):
        use_item()
    elif (action == "move"):
        player_move()
    else: 
        print (f"{action} is an invalid action")


  