from creatures.creature import Creature

class Hero(Creature):
    def __init__(self, nom, pv, defense, initiative, type_degats, arme):
        super().__init__(nom, pv, defense, initiative, type_degats)
        self.arme = arme
        self.inventaire = []

    def afficher_caracteristiques(self):
        super().afficher_caracteristiques()
        print(f"Arme: {self.arme}")