from Position import Position
from Animal import Animal
from copy import copy
from SosnowskyBorscht import SosnowskyBorscht


class CyberSheep(Animal):

    def __init__(self, world, position, strength=11):
        super().__init__(world, position, 'blue violet', 'CyberSheep', 4, strength, -1, 1)

    def find_nearest_borscht(self):
        position = copy(self.position)
        min_distance = 40
        closest_borscht = None
        for y in range(20):
            for x in range(20):
                position_check = Position(x, y)
                organism = self.get_organism_on_board(position_check)
                if organism is not None:
                    if isinstance(organism, SosnowskyBorscht):
                        distance = abs(position.x - position_check.x) + abs(position.y - position_check.y)
                        if distance < min_distance:
                            min_distance = distance
                            closest_borscht = position_check
        return closest_borscht

    def action(self):
        nearest_borscht = self.find_nearest_borscht()
        if nearest_borscht is None:
            super().action()
        else:
            position = copy(self.position)
            destination = copy(nearest_borscht)
            if destination.x < position.x and destination.y < position.y:
                direction = 0
            if destination.x >= position.x and destination.y <= position.y:
                direction = 1
            if destination.x >= position.x and destination.y > position.y:
                direction = 2
            if destination.x < position.x and destination.y >= position.y:
                direction = 3
            if self.check_if_can_move(direction):
                new_position = self.compute_new_position(direction)
                if self.is_collision(new_position):
                    self.collision(new_position)
                else:
                    self.move(new_position)
