import os
from colorama import Fore, Style, init
import shops
import items
import player
from status import status_bar
# "": {"price":, "stock":},
# self.print_item(self.blacksmith, "")

class Shopkeeper:
    def __init__(self):
        init(autoreset=True)



    def print_item(self, shop, item, counter=None):
        if counter != None:
            counter = str(counter) + ". "
        else:
            counter = ""
        print(f'{counter}{item: <17}{shop[item]["price"]: <10}{shop[item]["stock"]: <10}')


    def list_shop(self, shop):
        self._ = list(shop)
        self.counter = 1
        print(f'{"Item": <20}{"Price": <10}{"Stock": <10}')
        print(f'0. Return')
        for i in self._:
            self.print_item(shop, i, self.counter)
            self.counter += 1
    
    def buy_item(self, shop, item):
        shop[item]["stock"] -= 1
        print(f'Succesfully bought {item}.')

    def replenish_item(self, shop, item):
        shop[item]["stock"] += 1

    def looking(self, shop):
        os.system('cls')
        status_bar()
        self.list_shop(shop)
        print("\nWhould you like to purchase an item or return?")
        for i in range(1):
            while True:
                self._ = int(input("--> "))
                if self._ == 0:
                    break
                elif self._ <  0 or self._ > len(list(shop)):
                    print(f'Please enter only 1-{len(list(shop))}')
                else:
                    break
            self._ -= 1
            self.item = list(shop)[self._]
            
            

            if player.gold - shop[self.item]["price"] >= 0:
                player.gold -= shop[self.item]["price"]
                player.inventory[self.item] += 1
                shop[self.item]["stock"] -= 1
                print(f'\nSuccesfully bought 1 {self.item}')
            else:
                print(f"\nYou dont have enough gold to buy 1 {self.item}")
            input("\nPress 'Return' to return")
        