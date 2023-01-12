from shopkeeper_class import Shopkeeper
import os
from colorama import Fore, Style, init
import shops
import game
import items
import player


init(autoreset=True)
shopkeeper = Shopkeeper()
game_functions = game.Game_functions()



def main():
    os.system('cls')
    game_functions.start()






if __name__ == "__main__":
    main()