#Assign hero variables for health, attack moves, the damage of the attacks and the inventory
#Track monsters and their health (goblin 30, dragon 200)
# Display hero and master stats at the start
#Allow for ins and functions for attacking and using an item
# Create a graphical grid representation for the game wolrd, player position needs to be indicated and the player needs to be able to move 

# REMEMEBER ALL VARIABLES ARE CASE SENSITIVE SO APPLY THIS LOGIC WHEN WRITING CODE

#Hero stats shown in a dictionary 

from hero import Hero 
player = Hero()
player.attack()

hero_stats = {
    "name" : "hero", #key : value (name -> key) : (hero -> value)
    "strength" : 7,
    "health" : 100.0,
}

hero_max_health = 100

health_potion_strength = 5

#The hero inventory is written in a list because a list can be modified

hero_inventory = ["sword", "health potion", "rope"]

enemy_health = {
    "Evil Wizard": 100,
    "Magnificent Dragon": 200,
    }

#Defining functions

def quit ():
    print ("You Chose to Flee, You Are a Coward!\n")
    print ("GAME OVER!")
    return False

def player_stats (): 
    print ("You are:")
    for key, value in hero_stats.items():
        print(f"{key} : {value}" )

def player_move():
    pass

def player_attack():
    pass 

#MY OWN CODE TRYING TO SEE IF I CAN GET IT TO WORK 
isEquipped = False 

def player_equip_sword(isEquipped, item_name):

    if (hero_inventory.count("sword") <= 0):
        print (f"You don't have a {item_name}")
        return isEquipped
    
    #if (hero_inventory.count("sword") > 0):
     #   print (f"You have a sword, would you like to equip it?")

    else:
        hero_inventory.remove("sword")

        print(f"You have equipped the {item_name}, you can now attack enemies!")

        print(f"Your inventory is now {hero_inventory}")
        
        return True
    


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
            global isEquipped
            isEquipped = player_equip_sword(isEquipped, item_name)

        case "health potion":
            player_heal(item_name)

        case "rope":
            pass 

        case _: 
            print(f"{item_name} is not in your inventory")


#Temporary Function for damaging player

def damage_player(): 
    hero_stats["health"] = hero_stats["health"] - 10
    print(f"Your Health is now {hero_stats['health']}")


isPlaying = True

hero_stats["name"] = input ("What is your name?\n")

player_stats()

#this is from the loop dictionaries slide I need to understand this fully before moving on to next section 
print("\nEnemy health:")
for enemy, health in enemy_health.items():
    print(f"{enemy.capitalize()} has {health} health.")

#While loop for having the game running 

while (isPlaying):

    action = input("\nSelect Action: Attack, Use, Move & Flee\n").lower()

    print(f"Player Action: {action}")

    #The above code is an f string LOOK UP DOCUMENTATION FOR THIS 

    if (action == "flee"):
        isPlaying = quit() #<-- isPlaying = False 

    elif (action == "attack"):
        if isEquipped:
        #player_attack() temporary commented out to test code 
            damage_player()
        else: 
            print (f"You do not have a weapon equipped, please equip a weapon to be able to attack!")
    elif (action == "use"):
        use_item()
    elif (action == "move"):
        player_move()
    else: 
        print (f"{action} is an invalid action") 