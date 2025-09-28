#Character --> Hero
#        |____ Enemy 

#Player Heal
#Use items
#Connect the class to the main code (connect the files)
from character import Character

class Hero(Character):
    def __init__(self):

        super().__init__()
        #super.retreat()
        #self.max_health = 100.0 
        #move health_potion_strength to a diff class
        self.health_potion_strength = 5
        self.stats = {
            "name" : "Hero",
            "strength" : 7,
            "health" : 100.0,
        }

        self.inventory = ["sword", "health potion", "rope"]
    
    def print_stats(self):
        print("Your stats are: ")
        for key, value in self.stats.items():
            print(f"{key} : {value}")

    def set_name(self, name):
        self.stats["name"] = name
        self.print_stats()
    
    def move(self):
        pass

    def attack(self):
        pass 

    isEquipped = False 

    def equip_sword(self, isEquipped, item_name):

        if (self.inventory.count("sword") <= 0):
            print (f"You don't have a {item_name}")
            return isEquipped
        
        #if (hero_inventory.count("sword") > 0):
        #   print (f"You have a sword, would you like to equip it?")

        else:
            self.inventory.remove("sword")

            print(f"You have equipped the {item_name}, you can now attack enemies!")

            print(f"Your inventory is now {self.inventory}")
            
            return True

#needs to be worked on more was def damage player in other script 
    def take_damage(self, damage):
        self.stats["health"] = self.stats["health"] - damage
        print(f"Your Health is now {self.stats['health']}")
        pass
#move to use item function
    def heal(self, item_name):

        if (self.inventory.count("health potion") <= 0):
            print (f"You don't have any {item_name}")

        print (f"You've used a {item_name} you've restored {self.health_potion_strength} Health!")
        self.stats["health"] = self.stats["health"] + self.health_potion_strength

        if (self.stats["health"] >= self.max_health):
            print ("You've at Max health you don't need a health potion!")
            self.stats["health"] = self.max_health

        else:
            self.inventory.remove("health potion")

            print(f"You have used a {item_name}, your health is now {self.stats['health']}")
            
            print(f"Your inventory is now {self.inventory}")

    def use_item(self): 
        item_name = input(f"What item do you want to use? {self.inventory}\n")
        print (f"The item you want to use is {item_name}")
        match item_name:

            case "sword":
                global isEquipped
                isEquipped = self.equip_sword(isEquipped, item_name)

            case "health potion":
                self.heal(item_name)

            case "rope":
                pass 

            case _: 
                print(f"{item_name} is not in your inventory")

def main():
    print ("This is where our program/game starts!")
    hero = Hero()
    hero.print_stats()
    print("\n-----------------------------------------")
    hero.set_name("Britney Bitch")
    print("\n-----------------------------------------")
    hero.stats["health"] = 70
    print("\n-----------------------------------------")
    hero.heal("health potion")
    print("\n-----------------------------------------")
    print (f"{hero.max_health}")
    #hero.retreat()
    
if __name__ == '__main__':
    main()

#-----------------------------
#THIS IS TO TEST THE CLASS IS WORKING

