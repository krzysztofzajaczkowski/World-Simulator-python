from Position import Position
from abc import ABC, abstractmethod
from random import randint
from Organism import Organism


class Plant(Organism):

    def __init__(self, world, position, color, species, strength=0):
        super().__init__(world, position, color, 'Plant', species, 0, strength, -1, 0)
        self.type = 'Plant'
        self.initiative = 0
        self.add_organism_on_board()

    def randomize_if_spreading(self):
        chance_on_spreading = randint(1, 100)
        return chance_on_spreading > 90

    def multiply(self, partner=None):
        child_position = self.look_for_neighboring_free_field()
        if child_position is not None:
            if child_position.is_valid():
                message = self.species + ' is born on (' + str(child_position.x) + ',' + str(child_position.y) + ')'
                self.add_message_to_log(message)
                child = self.copy(self.world, child_position)
                self.spread(child)

    def spread(self, child):
        self.world.add_organism_to_world(child)

    def action(self):
        if self.randomize_if_spreading():
            self.multiply()

    def collision(self, position):
        attacker = self.get_organism_on_board(position)
        self.react_on_collision(attacker)

    def react_on_collision(self, attacker):
        defender_position = self.position
        message = attacker.species + ' has eaten ' + self.species + ' on (' + str(defender_position.x) + ',' + \
                  str(defender_position.y) + ')'
        self.add_message_to_log(message)
        self.die()
        attacker.move(defender_position)
