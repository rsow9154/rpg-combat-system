class Attack:
    def __init__(self, name, damage_dice, damage_type):
        self.name = name
        self.damage_dice = damage_dice
        self.damage_type = damage_type

    def execute(self, attacker, target):
        """Exécute une attaque."""
        attack_roll = random.randint(1, 20)
        if attack_roll == 20:  # Critique
            damage = sum(random.randint(1, self.damage_dice) for _ in range(2))
            print(f"Attaque critique ! {attacker.name} inflige {damage} dégâts à {target.name}.")
        elif attack_roll == 1:  # Échec critique
            damage = sum(random.randint(1, self.damage_dice) for _ in range(1))
            print(f"Échec critique ! {attacker.name} s'inflige {damage} dégâts.")
            attacker.pv -= damage
        elif attack_roll >= target.defense:
            damage = sum(random.randint(1, self.damage_dice) for _ in range(1))
            print(f"{attacker.name} inflige {damage} dégâts à {target.name}.")
            target.pv -= damage
        else:
            print(f"{attacker.name} rate son attaque contre {target.name}.")