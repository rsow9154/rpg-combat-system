from creatures.hero import Hero
from creatures.monster import Monster
from combat.combat_manager import CombatManager
from actions.attack import Attack
from actions.heal import Heal
from actions.buff import Buff

def main():
    # Création des héros
    heros = [
        Hero("Guerrier", 30, 15, 0, "Tranchant", "Épée longue"),
        Hero("Mage", 20, 10, 0, "Magique", "Bâton magique")
    ]

    # Ajout des actions aux héros
    heros[0].ajouter_action(Attack("Attaque", heros[0], None))
    heros[0].ajouter_action(Buff("Buff Défense", heros[0], None, "defense", 2))
    heros[1].ajouter_action(Heal("Soin", heros[1], None))
    heros[1].ajouter_action(Buff("Buff Dégâts", heros[1], None, "degats", 3))

    # Création des monstres
    monstres = [
        Monster("Gobelin", 15, 12, 0, "Percant", []),
        Monster("Dragon", 50, 18, 0, "Feu", ["Feu", "Contondant"])
    ]

    # Initialisation du combat
    combat = CombatManager(heros, monstres)
    combat.afficher_ordre_tour()

    # Déroulement du combat
    while not combat.combat_termine():
        combat.executer_tour()

    # Résultat du combat
    if all(hero.est_ko() for hero in heros):
        print("Les monstres ont gagné !")
    else:
        print("Les héros ont gagné !")

if __name__ == "__main__":
    main()