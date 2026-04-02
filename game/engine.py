from game.combat import attack
from models.enemy import Enemy
from models.player_ import player_
import os
from utils.storage import save_game, load_game


def create_player():
    name = input('Enter your name: ')
    return player_(name)

def fight(player, enemy):

    # Initialize turn counter for temporary defense

    turn_counter = 0

    # Combat loop
    while player.hp > 0 and enemy.hp > 0:
        print(f'\n{player.name} VS {enemy.name}')
        while True:

            print(f'{player.name} HP: {player.hp}/{player.hpmax}')
            print('VS')
            print(f'{enemy.name} HP: {enemy.hp}/{enemy.hpmax}') 
            print('\n1 - Attack')
            print('2 - Heal')
            print('3 - Defend')
            print('4 - Run')
            choice = input('Choose: ')

            # Increment turn counter for temporary defense
            turn_counter += 1

            if turn_counter > 3:
                # Reset temporary defense after 3 turns
                player.reset_defense()

            if choice == '1':
                attack(player, enemy)
            elif choice == '2':
                player.heal(10)
            elif choice == '3':
                player.temporary_defense += 2
                
                turn_counter = 0
                
            elif choice == '4':
                print('You ran away')
                return

            if enemy.hp <= 0:
                print('Enemy defeated')
                
                break

            if enemy.hp > enemy.hpmax * 0.3:
                attack(enemy, player)
            else:
                enemy.heal(5)
                print(f'{enemy.name} heals for 5 HP!')

            attack(enemy, player)
            if player.hp <= 0:
                print('You died')

                break

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
            print(f'Welcome back, {Player.name}!')
        else:
            Player = create_player()
    else:
        Player = create_player()
    
    game_loop(Player)
    

            



