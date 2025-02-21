# 🎲 Projet POO - Système de combat RPG

Un système de combat simplifié inspiré de Donjons et Dragons, développé en Python en utilisant les concepts de programmation orientée objet (POO).

---

## 📥 Installation

1. Clonez le dépôt :
git clone https://github.com/rsow9154/rpg-combat-system.git


---

🎮 Fonctionnalités:

Créatures
Héros : Les héros ont des caractéristiques uniques (PV, défense, initiative, etc.) et peuvent utiliser des armes.

Monstres : Les monstres ont des résistances spécifiques (feu, poison, etc.) et des types de dégâts prédéfinis.

Actions
Attaque : Inflige des dégâts à une cible. Gère les réussites critiques (double dégâts) et les échecs critiques (dégâts auto-infligés).

Soin : Soigne une cible en lui redonnant des points de vie.

Buff : Augmente temporairement une caractéristique (défense ou dégâts).

Combat
Tour par tour : Les créatures jouent en fonction de leur initiative.

Gestion des cibles : Les créatures KO ne peuvent pas être ciblées.

---

🕹️ Comment jouer
Lance le jeu :

bash
# Assurez-vous d'abord d'installer les dépendances :
pip install -r requirements.txt

# Puis lancez le jeu :
python main.py

# Déroulement du combat :

Le programme détermine l'ordre des tours en fonction de l'initiative.

À chaque tour, tu choisis une action pour ton héros (attaquer, soigner, buff).

Les monstres attaquent automatiquement.

Fin du combat :

Le combat se termine lorsque tous les héros ou tous les monstres sont KO.
Le programme affiche le résultat (victoire ou défaite).

---

📂 Structure du projet
Projet POO - Système de combat RPG/
│
├── creatures/
│   ├── __init__.py
│   ├── creature.py
│   ├── hero.py
│   └── monster.py
│
├── actions/
│   ├── __init__.py
│   ├── attack.py
│   ├── heal.py
│   └── buff.py
│
├── combat/
│   ├── __init__.py
│   ├── combat_manager.py
│   └── initiative.py
│
├── main.py
└── README.md


📝 Contribuer
Si vous souhaitez contribuer au projet, suivez ces étapes :

Forkez le dépôt.

Créez une nouvelle branche pour vos modifications :

bash
git checkout -b nom-de-votre-branche
Faites vos modifications et committez-les :

bash
Copy
git commit -m "Description de vos modifications"
Poussez vos modifications vers votre fork :

bash
Copy
git push origin nom-de-votre-branche 

🙏 Remerciements
Inspiré par Donjons et Dragons.

Développé dans le cadre d'un projet de programmation orientée objet (POO).

