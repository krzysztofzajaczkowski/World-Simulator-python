from Plant import Plant
from copy import copy


class WolfBerries(Plant):

    def __init__(self, world, position):
        super().__init__(world, position, 'purple', 'WolfBerries', 99)

    def react_on_collision(self, attacker):
        defender_position = copy(self.position)
        message = attacker.species + ' has eaten ' + self.species + ' on (' + str(defender_position.x) + ',' + \
                  str(defender_position.y) + ') and died from poison'
        self.add_message_to_log(message)
        attacker.die()
        self.die()
