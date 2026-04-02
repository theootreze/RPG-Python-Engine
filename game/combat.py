def attack(attacker, defender):
    # Calculate damage, ensuring it doesn't go below 0
    damage = max(attacker.attack - (defender.defense + defender.temporary_defense), 0)
    print(f'{attacker.name} attacks {defender.name} for {damage} damage!')

    defender.take_damage(damage)