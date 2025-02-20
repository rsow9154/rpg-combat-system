class Debuff:
    def __init__(self, name, effect, defense_reduction=0):
        self.name = name
        self.effect = effect
        self.defense_reduction = defense_reduction

    def execute(self, caster, target):
        """Applique un debuff à la cible."""
        print(f"{caster.name} utilise {self.name} sur {target.name} !")
        print(f"Effet : {self.effect}")
        target.defense -= self.defense_reduction
        print(f"{target.name} perd {self.defense_reduction} points de défense !")