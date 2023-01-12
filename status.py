from colorama import Fore
import player

def status_bar(): # prints text at top with health, mana and gold
    print(f'{Fore.RED}Health: {player.health: <7}', end="")     # health
    print(f'{Fore.CYAN}Mana: {player.mana: <7}', end="")        # mana
    print(f'{Fore.YELLOW}Gold: {player.gold: <5}', end="\n\n")              # gold