from copy import copy
from random import randint
from Animal import Animal


class Antelope(Animal):

    def __init__(self, world, position, strength=4, cooldown=-1):
        super().__init__(world, position, 'saddle brown', 'Antelope', 4, strength, cooldown, 2)

    def action(self):
        direction = self.randomize_direction()
        new_position = copy(self.position)
        is_move_performed = False
        step_try = self.step
        while not is_move_performed and step_try > 0:
            if self.check_if_can_move(direction, step_try):
                is_move_performed = True
                new_position = self.compute_new_position(direction, step_try)
            step_try -= 1
        if is_move_performed:
            if self.is_collision(new_position):
                self.collision(new_position)
            else:
                self.move(new_position)

    def collision(self, position):
        organism_on_new_position = self.get_organism_on_board(position)
        if organism_on_new_position is not None:
            if organism_on_new_position.species is self.species:
                self.multiply(organism_on_new_position)
            else:
                is_escape_possible = False
                if self.is_escape(organism_on_new_position):
                    escape_position = self.look_for_neighboring_free_field()
                    if escape_position is not None:
                        is_escape_possible = True
                        self.escape(escape_position, organism_on_new_position)
                if not is_escape_possible:
                    organism_on_new_position.react_on_collision(self)

    def react_on_collision(self, attacker):
        is_escape_succeeded = False
        if self.is_escape(attacker):
            escape_position = self.look_for_neighboring_free_field()
            if escape_position is not None:
                is_escape_succeeded = True
                defender_position = self.position
                self.escape(escape_position, attacker)
                attacker.move(defender_position)
        if not is_escape_succeeded:
            super().react_on_collision(attacker)

    def is_escape(self, organism):
        if organism.species is not 'Plant':
            return randint(1, 100) > 50
        else:
            return False

    def escape(self, escape_position, attacker):
        defender_position = self.position
        message = self.species + ' has run away from ' + attacker.species + ' on (' + str(defender_position.x) + ',' + \
                  str(defender_position.y) + ')'
        self.add_message_to_log(message)
        self.move(escape_position)
