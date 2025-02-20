from combat.initiative import lancer_initiative
from actions.attack import Attack
from actions.heal import Heal
from actions.buff import Buff

class CombatManager:
    def __init__(self, heros, monstres):
        self.heros = heros
        self.monstres = monstres
        self.creatures = lancer_initiative(heros + monstres)

    def afficher_ordre_tour(self):
        print("Ordre de tour :")
        for creature in self.creatures:
            print(f"{creature.nom} - Initiative: {creature.initiative}")

    def combat_termine(self):
        return all(hero.est_ko() for hero in self.heros) or all(monstre.est_ko() for monstre in self.monstres)

    def executer_tour(self):
        for creature in self.creatures:
            if creature.est_ko():
                continue
            print(f"\nC'est au tour de {creature.nom}.")
            if creature in self.heros:
                self.tour_hero(creature)
            else:
                self.tour_monstre(creature)
            if self.combat_termine():
                break

    def tour_hero(self, hero):
        hero.afficher_actions()
        choix = int(input("Choisissez une action : ")) - 1
        action = hero.actions[choix]

        # Définir la cible
        if isinstance(action, Attack):
            cible = self.choisir_cible(self.monstres)
        elif isinstance(action, Heal) or isinstance(action, Buff):
            cible = self.choisir_cible(self.heros)
        else:
            cible = None

        if cible:
            action.cible = cible
            action.executer()

    def tour_monstre(self, monstre):
        # Les monstres attaquent toujours
        cible = self.choisir_cible(self.heros)
        if cible:
            Attack("Attaque", monstre, cible).executer()

    def choisir_cible(self, cibles):
        cibles_disponibles = [c for c in cibles if not c.est_ko()]
        if not cibles_disponibles:
            return None
        print("Cibles disponibles :")
        for i, cible in enumerate(cibles_disponibles):
            print(f"{i + 1}. {cible.nom} - PV: {cible.pv}")
        choix = int(input("Choisissez une cible : ")) - 1
        return cibles_disponibles[choix]