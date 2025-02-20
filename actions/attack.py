import random

class Attack:
    def __init__(self, nom, lanceur, cible):
        self.nom = nom
        self.lanceur = lanceur
        self.cible = cible

    def executer(self):
        jet_attaque = random.randint(1, 20)
        if jet_attaque == 20:  # Réussite critique
            degats = self.lanceur.calculer_degats() * 2
            print(f"Attaque critique ! {self.lanceur.nom} inflige {degats} dégâts à {self.cible.nom}.")
        elif jet_attaque == 1:  # Échec critique
            degats = self.lanceur.calculer_degats()
            self.lanceur.pv -= degats
            print(f"Échec critique ! {self.lanceur.nom} s'inflige {degats} dégâts.")
        elif jet_attaque > self.cible.defense:  # Attaque réussie
            degats = self.lanceur.calculer_degats()
            self.cible.pv -= degats
            print(f"{self.lanceur.nom} inflige {degats} dégâts à {self.cible.nom}.")
        else:  # Attaque ratée
            print(f"{self.lanceur.nom} rate son attaque contre {self.cible.nom}.")