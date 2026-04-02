class player_:
    def __init__(self, name = 'you', hp = 100, attack = 3, defense = 1, hpmax = 100):
        self.name = name
        self.hp = hp
        self.hpmax = hpmax
        self.attack = attack
        self.defense = defense
        self.temporary_defense = 0
        

    def take_damage(self, amount):
        self.hp -= amount

    def heal(self, amount):
        self.hp = min(self.hp + amount, self.hpmax)

    def add_temporary_defense(self, amount):
        self.temporary_defense += amount
        # Ensure temporary defense does not exceed a reasonable limit (e.g., 5 times the base defense)
        self.temporary_defense = min(self.temporary_defense, self.defense * 5) 


    def reset_defense(self):
        self.temporary_defense = 0
    