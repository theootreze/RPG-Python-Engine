from game.combat import attack
from models.enemy import Enemy
from models.player import player

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
            fight(player, enemy)

        elif choice == '2':
            break
            

            



