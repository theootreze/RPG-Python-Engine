class player:
    def __init__(self, name = 'you', hp = 10, attack = 1):
        self.name = name
        self.hp = hp
        self.attack = attack
        

    def take_damage(self, amount):
        self.hp -= amount

    def heal(self, amount):
        self.hp += amount
    