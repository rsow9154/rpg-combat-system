class CombatManager:
    def __init__(self, creatures):
        self.creatures = creatures
        self.current_turn = 0

    def next_turn(self):
        """Passe au tour suivant."""
        self.current_turn = (self.current_turn + 1) % len(self.creatures)

    def get_current_creature(self):
        """Retourne la créature dont c'est le tour."""
        return self.creatures[self.current_turn]

    def is_combat_over(self):
        """Vérifie si le combat est terminé."""
        heroes_alive = any(creature.pv > 0 for creature in self.creatures if isinstance(creature, Hero))
        monsters_alive = any(creature.pv > 0 for creature in self.creatures if isinstance(creature, Monster))
        return not heroes_alive or not monsters_alive