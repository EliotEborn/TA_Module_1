#Assign hero variables for health, attack moves, the damage of the attacks and the inventory
#Track monsters and their health (goblin 30, dragon 200)
# Display hero and master stats at the start
#Allow for ins and functions for attacking and using an item
# Create a graphical grid representation for the game wolrd, player position needs to be indicated and the player needs to be able to move 

#from hero import Hero 
#player = Hero()
#player.attack()

import random

hero_stats = {
    "name" : "hero", 
    "strength" : 50,
    "health" : 100.0,
}

hero = hero_stats

hero_max_health = 100

health_potion_strength = 5

hero_inventory = ["sword", "health potion", "rope"]

wizard_stats = {
    "name" : "Evil Wizard",
    "strength" : 10,
    "health" : 100.0,
}

wizard_max_health = 100

dragon_stats = {
    "name" : "Fire Dragon",
    "strength" : 20,
    "health" : 300,
}


#Defining functions

def exit ():
    print ("You Chose to Flee, You Are a Coward!\n")
    print ("GAME OVER!")
    return False

def player_stats (): 
    print ("You are:")
    for key, value in hero_stats.items():
        print(f"{key} : {value}" )

def display_enemy_stats (stats):
    print (f"The {stats["name"]} approaches, his stats are: ")
    for key, value in stats.items():
        print(f"{key} : {value}" )
    return #something

#def display_dragon_stats (dragon_stats):
    #print ("The Fire Dragon approaches, his stats are: ")
    #for key, value in dragon_stats.items():
        #print(f"{key} : {value}" )
    #return #something

#damage from enemy to player

def damage_player(enemy, hero_health):
    hero_health = hero_health - enemy["strength"]
    
    return hero_health

#SETTING UP PLAYER HEALTH NOT GOING BELOW 0
# move to where enemy attacks hero
# TODO: MOVE MOVE MOVE
if hero_stats["health"] < 0:
    hero_stats["health"] = 0 
    print(f"Your health has been reduced to 0, GAME OVER!")


#this now works yippee
def deal_damage(hero, enemy_health):
    #damage = - hero["strength"]

    # for key, value in wizard_stats.items():

    #     if "name" == "Evil Wizard":
    #         enemy_health = wizard_stats["health"]

    # for key, value in dragon_stats.items():
    #     if "name" == "Fire Dragon":
    #         enemy_health = dragon_stats["health"]

    enemy_health = enemy_health - hero["strength"]
    print(f"Enemy now has {enemy_health} health!")   

    return enemy_health
            

def player_move():
    pass



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

#this function sets up the randomization of which enemy the player will encounter
def pick_random_enemy():
    if random.randint(0,13) > 10:
        current_enemy_stats = dragon_stats
    else:
        current_enemy_stats = wizard_stats
    return current_enemy_stats

isPlaying = True

hero_stats["name"] = input ("What is your name?\n")

player_stats()
current_enemy_stats = pick_random_enemy()
display_enemy_stats(current_enemy_stats)


#While loop for having the game running 

while (isPlaying):
    print(f"Player Turn:\n")
    action = input("\nSelect Action: Attack, Use, Move & Flee\n").lower()

    print(f"Player Action: {action}")

    #The above code is an f string LOOK UP DOCUMENTATION FOR THIS 

    if (action == "flee"):
        isPlaying = exit() #<-- isPlaying = False 

    elif (action == "attack"):
        if isEquipped:
        #player_attack() #temporary commented out to test code 
            current_enemy_stats["health"] = deal_damage(hero, current_enemy_stats["health"])
            if current_enemy_stats["health"] <= 0:
               current_enemy_stats["health"] = 0
               print(f"The enemy has been slain!")
               quit()
        else: 
            print (f"You do not have a weapon equipped, please equip a weapon to be able to attack!")
    elif (action == "use"):
        use_item()
    elif (action == "move"):
        player_move()
    else: 
        print (f"{action} is an invalid action") 

    #this is now the enemy turn
    print(f"\nEnemy Turn:\n")

    hero_stats["health"] = damage_player(current_enemy_stats, hero_stats["health"])
    if hero_stats["health"] <= 0:
        hero_stats["health"] = 0 
        print(f"Your health has been reduced to 0, GAME OVER!")
        quit()
    else:
        print(f"{current_enemy_stats["name"]} has dealt {current_enemy_stats["strength"]}. You now have {hero_stats["health"]}")