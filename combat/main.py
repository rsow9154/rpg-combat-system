from ui.interface import Interface
from combat.initiative import InitiativeSystem
from combat.combat_manager import CombatManager
from creatures.hero import Hero
from creatures.monster import Monster

def main():
    Interface.display_welcome()
    choice = Interface.get_user_choice()

    if choice == "1":
        heroes = [Hero("Guerrier", 50, 15), Hero("Mage", 30, 10)]
        monsters = [Monster("Gobelin", 30, 10), Monster("Dragon", 100, 20)]

        selected_heroes = Interface.select_creatures(heroes)
        selected_monsters = Interface.select_creatures(monsters)

        initiative_system = InitiativeSystem()
        for hero in selected_heroes:
            initiative_system.add_creature(hero)
        for monster in selected_monsters:
            initiative_system.add_creature(monster)

        initiative_system.roll_initiative()
        combat_manager = CombatManager(initiative_system.get_order())

        while not combat_manager.is_combat_over():
            current_creature = combat_manager.get_current_creature()
            print(f"\nC'est au tour de {current_creature.name} !")
            Interface.display_combat_status(combat_manager.creatures)
            combat_manager.next_turn()

if __name__ == "__main__":
    main()