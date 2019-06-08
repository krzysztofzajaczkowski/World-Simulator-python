from Plant import Plant


class Guarana(Plant):

    def __init__(self, world, position):
        super().__init__(world, position, 'cyan', 'Guarana', 0)

    def improve_strenght_of_organism(self, organism):
        organism.strength += 3

    def react_on_collision(self, attacker):
        defender_position = self.position
        self.improve_strenght_of_organism(attacker)
        message = self.species + ' improved strength of ' + attacker.species + ' on (' \
                  + str(defender_position.x) + ',' + str(defender_position.y) + ')'
        self.add_message_to_log(message)
        self.die()
        attacker.move(defender_position)
