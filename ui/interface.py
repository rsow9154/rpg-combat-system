class Interface:
    @staticmethod
    def display_welcome():
        print("Bienvenue dans le système de combat RPG !")
        print("1. Démarrer un combat")
        print("2. Quitter")

    @staticmethod
    def get_user_choice():
        return input("Choisissez une option : ")
            @staticmethod
    def select_creatures(creatures):
        print("Sélectionnez les créatures pour le combat :")
        for i, creature in enumerate(creatures):
            print(f"{i + 1}. {creature.name}")
        choices = input("Entrez les numéros séparés par des virgules : ")
        return [creatures[int(choice) - 1] for choice in choices.split(",")]
     @staticmethod
    def display_combat_status(creatures):
        print("\nÉtat du combat :")
        for creature in creatures:
            print(f"{creature.name} : {creature.pv} PV")