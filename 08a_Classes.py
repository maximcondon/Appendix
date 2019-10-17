
from random import randint
import sys

HEALTHY = 1
WOUNDED = 2
DEAD = 3

class Player:
    # These are the attibutes: name, strength, health status...
    def __init__(self, name, strength=1):
        '''
        Here you set the initial attributes of your object
        It can take as many arguments as you need it to
        '''
        self.name = name
        self.strength = int(strength)
        self.status = HEALTHY
        assert strength > 0

    # These are the functions, or the methods that can be performed!
    def move(self, direction):
        print(f'{self.name} is moving to {direction}')

    def die(self):
        print(f'OMG! {self.name} has died!')
        sys.exit(1) # Terminates the program!

    def attack(self, monster):
        print(f'{self.name} is attacking {monster.name}')
        strength_player = self.strength + randint(1, 6)
        strength_monster = monster.strength + randint(1, 6)
        if strength_player > strength_monster:
            print(f'{self.name} beats {monster.name} to a pulp!')
        elif strength_player < strength_monster:
            if self.status == WOUNDED:
                self.die()
            print(f'{self.name} loses and is wounded!')
            self.status = WOUNDED
        else:
            print('You both retreat!')

    def heal(self):
        if self.status == WOUNDED:
            self.status = HEALTHY
            print(f'++Bling Bling++ {self.name} you are healed! ++Bling Bling++')

class Monster:

    def __init__(self, name, strength=1):
        self.name = name
        self.strength = int(strength)
        assert strength > 0

m1 = Monster('Zombie', 2)
m2 = Monster('Revenge Porn Pervert', 1)
m3 = Monster('Discrimination', 3)
m4 = Monster('Ganon', 4)

link = Player('Link', 2)
link.move('the bar')
link.move('the cave')
link.attack(m1)

zelda = Player('Zelda', 72)
zelda.move('the playground')
zelda.move('the courthouse')
zelda.attack(m2)
zelda.attack(m3)

for i in range(5):
    link.attack(m1)
    link.heal()
