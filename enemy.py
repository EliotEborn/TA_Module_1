from character import Character

class Enemy(Character):
    def __init__(self):

        super().__init__()
        self.attack_moves = {
            "Ice Shard" : 15,
            "Multi-Shock" : 20,
            "Poison Prison" : 25,
            "Basic Brawl" : 5,
        }
        self.stats = {
            "name" : "Evil Wizard",
            "strength" : 10,
            "health" : 100,
        }

    def print_stats(self):
        print ("The Evil Wizard approaches, his stats are: ")
        for key, value in self.stats.items():
            print (f"{key} : {value}")

    def attack(self, move_name):
        print (f"The Evil Wizard has attacked you with {move_name}")
        match move_name:

            case "Ice Shard":
                return self.attack_moves ["Ice Shard"]
                
            case "Multi-Shock":
                return self.attack_moves ["Multi-Shock"]

            case "Poison Prison":
                return self.attack_moves ["Poison Prison"]
            
            case "Basic Brawl":
                return self.attack_moves ["Basic Brawl"]


    def move(self):
        pass

    def take_damage(self, damage):
        self.stats["health"] = self.stats["health"] - damage 
        print (f"You've weakened the enemy, their health is now {self.stats['health']}")
        pass 

        if self.stats["health"] <= 0:
            print (f"The enemy has been slain!")



