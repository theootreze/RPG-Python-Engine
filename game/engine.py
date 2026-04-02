from game.combat import attack
from models.enemy import Enemy
from models.player import player
import os
from utils.storage import save_game, load_game


def create_player():
    name = input('Enter your name: ')
    return player(name)

def fight(player, enemy):
    while player.hp > 0 and enemy.hp > 0:
        attack(player, enemy)

        if enemy.hp <= 0:
            print('Enemy defeated')
            break
        attack(enemy, player)
    if player.hp <= 0:
        print('You died')

def game_loop(Player):
    while True:
        print('\n1 - Fight')
        print('2 - Exit')

        choice = input("Choose: ")

        if choice == '1' :

            enemy = Enemy()
            fight(Player, enemy)

        elif choice == '2':
            save_game(Player)
            break
            
def start_game():
    if os.path.exists('data/save.json'):
        choice = input('Load saved game? (y/n): ')
        if choice.lower() == 'y':
            Player = load_game()
        else:
            Player = create_player()
    else:
        Player = create_player()
    
    game_loop(Player)
    

            



