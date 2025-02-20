from creatures.creature import Creature

class Monster(Creature):
    def __init__(self, nom, pv, defense, initiative, type_degats, resistances):
        super().__init__(nom, pv, defense, initiative, type_degats)
        self.resistances = resistances

    def calculer_degats(self):
        degats = super().calculer_degats()
        if self.type_degats in self.resistances:
            degats = degats // 2
            print(f"{self.nom} résiste aux dégâts ! Dégâts réduits à {degats}.")
        return degats