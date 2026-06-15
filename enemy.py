import Dictionaries as dict
from abc import ABC, abstractmethod


class Enemy(ABC):
    def __init__(self, health, weapon, armor, ):
        self.harm = None
        self.damage = None
        self.health = health
        self.weapon = weapon
        self.armor = armor

    @abstractmethod
    def damage_dealt(self):
        pass

    @abstractmethod
    def harm_received(self, enemyDamage):
        pass


class Mage(Enemy):
    def damage_dealt(self):
        self.damage = dict.weapons.get(self.weapon)

    def harm_received(self, enemyDamage):
        self.harm = enemyDamage - dict.armors.get(self.armor)


class Knight(Enemy):
    def damage_dealt(self):
        self.damage = dict.weapons.get(self.weapon)

    def harm_received(self, enemyDamage):
        self.harm = enemyDamage - dict.armors.get(self.armor)


class Giant(Enemy):
    def damage_dealt(self):
        self.damage = dict.weapons.get(self.weapon)

    def harm_received(self, enemyDamage):
        self.harm = enemyDamage - dict.armors.get(self.armor)


class Archer(Enemy):
    def damage_dealt(self):
        self.damage = dict.weapons.get(self.weapon)

    def harm_received(self, enemyDamage):
        self.harm = enemyDamage - dict.armors.get(self.armor)