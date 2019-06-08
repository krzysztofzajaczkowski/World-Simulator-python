from Position import Position
from Plant import Plant


class SosnowskyBorscht(Plant):

    def __init__(self, world, position):
        super().__init__(world, position, 'magenta2', 'SosnowskyBorscht', 10)

    def react_on_collision(self, attacker):
        defender_position = self.position
        message = attacker.species + ' has eaten ' + self.species + ' on (' + str(defender_position.x) + ',' \
                  + str(defender_position.y) + ')'
        self.die()
        if attacker.species != 'CyberSheep':
            message += ' and died from poison'
            attacker.die()
        else:
            attacker.move(defender_position)
        self.add_message_to_log(message)

    def kill_if_animal(self, position):
        victim = self.get_organism_on_board(position)
        if victim is not None:
            if victim.type == 'Animal' and victim.species != 'CyberSheep':
                victim_position = victim.position
                message = self.species + ' kills ' + victim.species + ' on (' + str(victim_position.x) + ',' + str(
                    victim_position.y) + ')'
                self.add_message_to_log(message)
                victim.die()

    def kill_neighbors(self):
        position = self.position
        for dx in range(-1, 1):
            for dy in range(-1, 1):
                if not (dx == 0 and dx == dy):
                    killing_position = Position(position.x + dx, position.y + dy)
                    if killing_position.is_valid():
                        self.kill_if_animal(killing_position)

    def action(self):
        self.kill_neighbors()
        super().action()
