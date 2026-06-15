import Dictionaries as dict
from abc import ABC, abstractmethod


class Enemy(ABC):
    def __init__(self, health: int, weapon: str, armor: str, dropped_items: list):
        self.harm = None
        self.damage = None
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.dropped_items = dropped_items

    @abstractmethod
    def damage_dealt(self):
        pass

    @abstractmethod
    def harm_received(self, enemyDamage):
        pass

    @abstractmethod
    def items_dropped(self):
        pass


class Mage(Enemy):
    def damage_dealt(self):
        self.damage = dict.weapons.get(self.weapon)

    def harm_received(self, enemyDamage):
        self.harm = enemyDamage - dict.armors.get(self.armor)

    def items_dropped(self):
        self.dropped_items.extend([self.weapon, self.armor])


class Knight(Enemy):
    def damage_dealt(self):
        self.damage = dict.weapons.get(self.weapon)

    def harm_received(self, enemyDamage):
        self.harm = enemyDamage - dict.armors.get(self.armor)

    def items_dropped(self):
        self.dropped_items.extend([self.weapon, self.armor])


class Giant(Enemy):
    def damage_dealt(self):
        self.damage = dict.weapons.get(self.weapon)

    def harm_received(self, enemyDamage):
        self.harm = enemyDamage - dict.armors.get(self.armor)

    def items_dropped(self):
        self.dropped_items.extend([self.weapon, self.armor])

# Archer class
class Archer(Enemy):
    def damage_dealt(self):
        self.damage = dict.weapons.get(self.weapon)

    def harm_received(self, enemyDamage):
        self.harm = enemyDamage - dict.armors.get(self.armor)

    def items_dropped(self):
        self.dropped_items.extend([self.weapon, self.armor])