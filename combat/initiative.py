def lancer_initiative(creatures):
    for creature in creatures:
        creature.lancer_initiative()
    creatures.sort(key=lambda x: x.initiative, reverse=True)
    return creatures