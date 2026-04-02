import json

def save_game(player):
    data = {
        "name": player.name,
        "hp": player.hp,    
        "attack": player.attack,
        "defense": player.defense,
        "hpmax": player.hpmax

    }
    with open('data/save.json', 'w') as f:
        json.dump(data, f)
    
    print('Game saved.')

from models.player_ import player_

def load_game():
    with open('data/save.json', 'r') as f:
        data = json.load(f)
    return player_(data['name'], data['hp'], data['attack'], data['defense'], data['hpmax'])