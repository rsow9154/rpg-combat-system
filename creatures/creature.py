import random

class Creature:
    def __init__(self, nom, pv, defense, initiative, type_degats):
        self.nom = nom
        self.pv = pv
        self.defense = defense
        self.initiative = initiative
        self.type_degats = type_degats
        self.etats = []
        self.actions = []  # Liste des actions disponibles
        self.degats = 0  # Ajout de l'attribut degats

    def lancer_initiative(self):
        self.initiative = random.randint(1, 20)
        return self.initiative

    def ajouter_action(self, action):
        self.actions.append(action)

    def afficher_actions(self):
        print(f"Actions disponibles pour {self.nom} :")
        for i, action in enumerate(self.actions):
            print(f"{i + 1}. {action.nom}")

    def calculer_degats(self):
        # Par défaut, on utilise 1d6 pour les dégâts
        return random.randint(1, 6)

    def est_ko(self):
        return self.pv <= 0

    def afficher_caracteristiques(self):
        print(f"{self.nom} - PV: {self.pv}, Défense: {self.defense}, Initiative: {self.initiative}")