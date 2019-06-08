from Position import Position
from random import randint
from Animal import Animal
from copy import copy


class Turtle(Animal):

    def __init__(self, world, position, strength=2):
        super().__init__(world, position, 'dark green', 'Turtle', 1, strength, -1, 1)

    def action(self):
        chance_to_move = randint(1, 100)
        if chance_to_move > 75:
            super().action()

    def collision(self, position):
        organism_on_position = self.get_organism_on_board(position)
        if organism_on_position is not None:
            if organism_on_position.species == self.species:
                self.multiply(organism_on_position)
            else:
                if not self.is_attack_repelled(organism_on_position):
                    organism_on_position.react_on_collision(self)
                else:
                    message = self.species + ' repels ' + organism_on_position.species + \
                              ' on (' + str(position.x) + ',' + str(position.y) + ')'
                    self.add_message_to_log(message)
        else:
            self.move(position)

    def is_attack_repelled(self, opponent):
        return opponent.strength < 5 and opponent.type == 'Animal'

    def react_on_collision(self, attacker):
        position = copy(self.position)
        if not self.is_attack_repelled(attacker):
            super().react_on_collision(attacker)
        else:
            message = self.species + ' repels ' + attacker.species + \
                      ' in defense on (' + str(position.x) + ',' + str(position.y) + ')'
            self.add_message_to_log(message)
