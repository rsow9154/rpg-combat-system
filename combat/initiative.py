import random

def roll_dice(sides=20):
    """Lance un dé avec un nombre de faces donné."""
    return random.randint(1, sides)

class InitiativeSystem:
    def __init__(self):
        self.creatures = []

    def add_creature(self, creature):
        """Ajoute une créature au système d'initiative."""
        self.creatures.append(creature)

    def roll_initiative(self):
        """Lance l'initiative pour toutes les créatures."""
        for creature in self.creatures:
            creature.initiative = roll_dice()
        self.creatures.sort(key=lambda x: x.initiative, reverse=True)

    def get_order(self):
        """Retourne l'ordre des créatures en fonction de leur initiative."""
        return self.creatures