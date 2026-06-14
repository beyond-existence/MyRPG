import Dictionaries as dict

class Player:
    def __init__(self, health, weapon, armor):
        self.harm = None
        self.damage = None
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def damage_dealt(self):
        self.damage = dict.weapons.get(self.weapon)

    def harm_received(self, enemyDamage):
        self.harm = enemyDamage - dict.armors.get(self.armor)