import shops
import player
import items
from shopkeeper_class import Shopkeeper
import os
from colorama import Fore, Style, init
from status import status_bar
import random
from time import sleep
shopkeeper = Shopkeeper()


class Game_functions:
    
    def __init__(self):
        init(autoreset=True)
        


    def town(self):
        os.system('cls')
        status_bar()
        print("Shops")
        print("1. Blacksmith")
        print("2. Fletcher")
        print("3. Magic Shop")
        print("4. Butcher")
        print("5. Shoemaker")
        print("6. Return")

    def list_inventory(self):
        os.system('cls')
        status_bar()
        print(f'{"Item": <20}{"Amount": <10}{"Damage": <10}{"Defense": <10}', end="\n\n")
        for i in player.inventory:
            if player.inventory[i] >= 1:
                print(f'{i: <20}', end="")
                print(f'{player.inventory[i]: <10}', end="")
                print(f'{items.items[i]["damage"]: <10}', end="")
                print(f'{items.items[i]["defense"]: <10}') 
        
        input("\nPress 'Return' to return")
        self.start()


    def start(self):
        failed = False
        while(True):
            os.system('cls')
            status_bar()
            print("What would you like to do?")
            print("1. Go to town")
            print("2. Fight Monster")
            print("3. Look in backpack")

            self._ = input("--> ")
            
            if failed == True:
                print("Please enter only 1, 2 or 3")

            if self._ == "1":
                self.shopping()
                break
            elif self._ == "2":
                os.system('cls')
                self.combat()
                break
            elif self._ == "3":
                self.list_inventory()
                break
            else:
                print("Please enter only 1, 2 or 3")
                sleep(1)
                
            

    def shopping(self):
        os.system('cls')
        status_bar()
        self.town()
        
        self._ = int(input("--> "))
        os.system('cls')
        status_bar()
        if self._ == 1:
            shopkeeper.list_shop(shops.blacksmith)
            shopkeeper.looking(shops.blacksmith)
        elif self._ == 2:
            shopkeeper.list_shop(shops.fletcher)
            shopkeeper.looking(shops.fletcher)
        elif self._ == 3:
            shopkeeper.list_shop(shops.magic_shop)
            shopkeeper.looking(shops.magic_shop)
        elif self._ == 4:
            shopkeeper.list_shop(shops.butcher)
            shopkeeper.looking(shops.butcher)
        elif self._ == 5:
            shopkeeper.list_shop(shops.shoemaker)
            shopkeeper.looking(shops.shoemaker)
        else:
            self.start()
        self.start()



    def flee(self, monster):
        status_bar()
        self._ = random.random()
        if self._ > 0.3:
            print(f'You succesfully fled from the {monster}')
            input("Press 'Return' to return")
            os.system('cls')
            self.start()
        else:
            print("Flee failed")
            input("Press 'Return' to return")
            os.system('cls')
            self.combat(1)

    def combat(self, flee=0):
        if flee == 0:
            self._ = random.randint(0,21)
            self.mob = (list(items.mobs))
            self.mob_stats = items.mobs[self.mob[self._]]

        fighting = True
        self.attacks = ""

        while(fighting == True):

            self.failed = False

            os.system('cls')

            player.health -= self.mob_stats["damage"]
            if player.health <= 0:
                player.dead = True
                player.health = 0

            status_bar()

            print(f"You've encountred a {self.mob[self._]}")
    #        print(self.mob_stats)
            print(f'Health: {self.mob_stats["health"]: <6}Defense: {self.mob_stats["defense"]: <4}Damage: {self.mob_stats["damage"]: <4}Evasion: {self.mob_stats["evasion"]: <4}')
            

            
            self.attack = f'{self.mob[self._]} attacked you and dealt {self.mob_stats["damage"]} damage'
            self.attacks = self.attacks + "\n" + self.attack
            print(self.attacks)
            if player.health <= 0:
                print("\nYou died")
                input("Press 'Return' to return")
                self.start()
            print("\nWhat whould you like to do?")
            print("1. Attack")
            print("2. Flee")


            while True:
                print(f'{"": <100}', end="\r")
                self.__ = input("--> ")


                if self.__ == "1":
                    print("")
                    print(f'You attacked {self.mob[self._]} with {player.equipped_item_name} and dealt {player.equipped_item["damage"]} damage')
                    break
                elif self.__ == "2":
                    os.system('cls')
                    self.flee(self.mob[self._])
                    break
                else:
                    print("Please enter only 1 or 2", end="\r")
                    sleep(1)