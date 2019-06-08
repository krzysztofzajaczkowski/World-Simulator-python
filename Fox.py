from Position import Position
from Animal import Animal
from copy import copy


class Fox(Animal):

    def __init__(self, world, position, strength=3):
        super().__init__(world, position, 'orange', 'Fox', 7, strength, -1, 1)
        self.strength = strength
        self.initiative = 7
        self.species = 'Fox'
        self.color = 'orange'

    def is_safe(self, position):
        attacker = self.get_organism_on_board(position)
        if attacker is not None:
            return self.strength >= attacker.strength
        return True

    def find_any_safe_field(self):
        position = copy(self.position)
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if not (dx == 0 and dx == dy):
                    safe_position = Position(position.x + dx, position.y + dy)
                    if safe_position.is_valid():
                        if self.is_collision(safe_position):
                            if self.is_safe(safe_position):
                                return safe_position
                        else:
                            return safe_position
        return self.position

    def find_safe_field(self):
        direction = self.randomize_direction()
        if self.check_if_can_move(direction):
            new_position = self.compute_new_position(direction)
            if self.is_collision(new_position):
                if self.is_safe(new_position):
                    return new_position
                else:
                    self.find_any_safe_field()
            else:
                return new_position

    def action(self):
        new_position = self.find_safe_field()
        if new_position is not None:
            if new_position != self.position:
                if self.is_collision(new_position):
                    self.collision(new_position)
                else:
                    self.move(new_position)
