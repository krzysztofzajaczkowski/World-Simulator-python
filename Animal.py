from Organism import Organism


class Animal(Organism):

    def __init__(self, world, position, color, species, initiative, strength, cooldown=-1, step=1):
        super().__init__(world, position, color, 'Animal', species, initiative, strength, cooldown, step)
        self.world.add_organism_on_board(self)

    def give_birth(self, child):
        self.world.add_organism_to_world(child)

    def react_on_collision(self, attacker):
        defender_position = self.position
        if attacker.strength >= self.strength:
            message = attacker.species + ' has won with ' + self.species + ' on (' + str(defender_position.x) + ',' + \
                      str(defender_position.y) + ')'
            self.add_message_to_log(message)
            self.die()
            attacker.move(defender_position)
        else:
            message = attacker.species + ' has lost with ' + self.species + ' on (' + str(defender_position.x) + ',' + \
                      str(defender_position.y) + ')'
            self.add_message_to_log(message)
            attacker.die()

    def action(self):
        direction = self.randomize_direction()
        if self.check_if_can_move(direction):
            new_position = self.compute_new_position(direction)
            if self.is_collision(new_position):
                self.collision(new_position)
            else:
                self.move(new_position)

    def collision(self, position):
        organism_on_new_position = self.get_organism_on_board(position)
        if organism_on_new_position is not None:
            if organism_on_new_position.species == self.species:
                self.multiply(organism_on_new_position)
            else:
                organism_on_new_position.react_on_collision(self)

    def multiply(self, partner):
        child_position = self.look_for_neighboring_free_field()
        if child_position is None:
            child_position = partner.look_for_neighboring_free_field()
        if child_position is not None:
            message = self.species + ' is born on (' + str(child_position.x) + ',' + str(child_position.y) + ')'
            self.add_message_to_log(message)
            child = self.copy(self.world, child_position)
            self.give_birth(child)
