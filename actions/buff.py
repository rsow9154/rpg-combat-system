class Buff:
    def __init__(self, nom, lanceur, cible, stat, valeur):
        self.nom = nom
        self.lanceur = lanceur
        self.cible = cible
        self.stat = stat  # Exemple : "defense", "degats"
        self.valeur = valeur  # Exemple : +2

    def executer(self):
        if self.stat == "defense":
            self.cible.defense += self.valeur
            print(f"{self.lanceur.nom} augmente la défense de {self.cible.nom} de {self.valeur}.")
        elif self.stat == "degats":
            self.cible.degats += self.valeur
            print(f"{self.lanceur.nom} augmente les dégâts de {self.cible.nom} de {self.valeur}.")