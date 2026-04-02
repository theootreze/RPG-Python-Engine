class player:
    def __init__(self, name = 'you', hp = 100, attack = 3):
        self.name = name
        self.hp = hp
        self.attack = attack
        

    def take_damage(self, amount):
        self.hp -= amount

    def heal(self, amount):
        self.hp += amount
    