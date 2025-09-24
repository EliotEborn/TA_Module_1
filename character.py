#Character ___ Hero
# Enemy 

class Hero (): 
    def __init__(self):
        self.stats =  {
            "name" : "hero", 
            "strength" : 7,
            "health" : 100.0
        }

        self.inventory = ["sword", "health potion", "rope"]   
    
    def print_stats(self):
        print ("Your stats are: ")
        for key, value in self.stats.items():
            print(f"{key} : {value}")

    def set_name(self, name):
        self.stats["name"] = name
        self.print_stats()

    def move(self):
        pass 

    def attack(self):
        pass

    def take_damage(self, damage):
        self.stats["health"] = self.stats["health"] - damage
        print (f"Your Health is now {self.stats['health']}")
        pass 

    def heal(self):
        
        if (self.inventory.count("health potion")<= 0):
            print(f"You don't have any {item_name}")

    print (f"You've used a {item_name}")

    def use_item(self):
        pass 




#--------------------------------------------------------  

player = Hero()

print (f"Here are your Hero Stats {player.stats}")