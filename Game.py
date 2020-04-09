from abc import ABC, abstractmethod
import random
class Unit(ABC):
    _name = None
    _strength = 0
    _health = 0

    def _cheak_name(self, name):
        return name

    def __init__(self, name, strength, health):
        self._name = self._cheak_name(name)
        self._strength = strength
        self.health = health

    @abstractmethod
    def _attack(self, opponent):
        pass

    def attack(self, opponent):
        if not isinstance(opponent, Unit):
            raise Exception
        if opponent._health == 0:
            raise Exception(f'Здоровье противника = "{opponent.health}"')

        if isinstance(opponent, Rogue):
            r = random.randint(1, 10)
            if r == 2:
                opponent.health = opponent.health
            else:
                return self._attack(opponent)
        else:
            return self._attack(opponent)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, val):
        if not isinstance(val, (int,float)):
            raise Exception

        self._health = val if val > 0 else 0

class Vampire(Unit):

    def _attack(self, opponent):
        dmg = self._strength
        opponent.health -= dmg
        self.health += dmg * 0.1

class Knight(Unit):

    def _attack(self, opponent):

        dmg = self._strength
        opponent.health -= dmg

class Monk(Unit):

    def _attack(self, opponent):
        dmg = opponent._strength
        opponent.health -= dmg
        self._health = round(self._health * 1.1)

class Rogue(Unit):

    def _attack(self, opponent):
        dmg = self._strength
        opponent.health -= dmg

k1 = Knight(name="Artur", strength=100, health=100000)
v1 = Vampire(name="Drac", strength=10, health=1000)
r1 = Rogue(name="Krok", strength=150, health=2000)
m1 = Monk(name="Panda Kunfu", strength=90, health=1000)

print(m1.health)

m1.attack(k1)
print(m1.health)
m1.attack(k1)
print(m1.health)
m1.attack(k1)
print(m1.health)
m1.attack(k1)
print(m1.health)
m1.attack(k1)
print(m1.health)
m1.attack(k1)
print(m1.health)

