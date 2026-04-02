class Enemy:
    def __init__(self, name = 'Monster', hp = 10, attack = 10):
        self.name = name
        self.hp = hp
        self.hpmax = hp
        self.attack = attack
        self.defense = 1
    
    def take_damage(self, amount):
        self.hp -= amount
    
    def heal(self, amount):
        # Heal the enemy, but not above its maximum HP
        self.hp = min(self.hp + amount, self.hpmax)
        