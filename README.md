# RPG Python Engine

terminal-based RPG system built in python with modular architecture and save/load functionality.

## Game Flow

1. Start game
2. Check if save file exists
3. if exists:
    - Ask user to load
4. If not:
    - Create new player
5. Enter main loop:
    - player chooses action
    - Actions:
        - Fight enemy
        - save game
        - exit
6. Repeat until exit or death

## Architecture

### Engine.py
controls the game flow:
- game start
- main loop
- user input handling

### combat.py
handles combat logic:
- attack calculations
- HP reduction

### player.py
Represents player data:
- name
- HP
- attack

### enemy.py
Represents enemies:
- same structure as player

### storage.py
Handles persistence
- save game to JSON
- load game from JSON

## Save Structure

'''json
{
    "name": "player",
    "hp": 100,
    "attack": 10
}