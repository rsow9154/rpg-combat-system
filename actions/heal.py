import random

class Heal:
    def __init__(self, nom, lanceur, cible):
        self.nom = nom
        self.lanceur = lanceur
        self.cible = cible

    def executer(self):
        soin = random.randint(1, 8)  # Soin de 1d8
        self.cible.pv += soin
        print(f"{self.lanceur.nom} soigne {self.cible.nom} de {soin} PV.")