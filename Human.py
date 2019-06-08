from copy import copy
from Position import Position
from Animal import Animal
from Organism import Organism


class Human(Animal):
    
    def __init__(self, world, position, strength=4, cooldown=0):
        super().__init__(world, position, 'DarkGoldenrod4', 'Human', 4, strength, cooldown)
        if cooldown > 5:
            self.skill_active = True
            self.color = 'Red'
        else:
            self.skill_active = False
        self.chosen_action = None

    @property
    def skill_active(self):
        return self._skill_active

    @skill_active.setter
    def skill_active(self, value):
        self._skill_active = value
        
    @property
    def chosen_action(self):
        return self._chosen_action

    @chosen_action.setter
    def chosen_action(self, action):
        self._chosen_action = action

    def action(self):
        if self.cooldown <= 5:
            self.deactivate_skill()
        if self.skill_active:
            self.color = 'red'
            self.burn_neighbors()
        self.perform_chosen_action()
        if self.skill_active:
            self.burn_neighbors()

    def burn_neighbors(self):
        position = copy(self.position)
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if not (dx == 0 and dx == dy):
                    position_to_burn = Position(position.x + dx, position.y + dy)
                    if position_to_burn.is_valid():
                        self.burn(position_to_burn)

    def burn(self, position):
        victim = self.get_organism_on_board(position)
        if isinstance(victim, Organism):
            message = self.species + ' burns ' + victim.species + ' on (' + str(position.x) + \
                      ',' + str(position.y) + ')'
            self.add_message_to_log(message)
            victim.die()

    def activate_skill(self):
        self.skill_active = True
        self.color = 'Red'
        self.add_organism_on_board()
        self.cooldown = 10

    def deactivate_skill(self):
        self.skill_active = False
        self.color = 'DarkGoldenrod4'
        self.add_organism_on_board()

    def perform_chosen_action(self):
        direction = -1
        if self.chosen_action == 'Up':
            direction = 0
        if self.chosen_action == 'Right':
            direction = 1
        if self.chosen_action == 'Down':
            direction = 2
        if self.chosen_action == 'Left':
            direction = 3
        if self.chosen_action == 'Skill':
            if self.cooldown == 0:
                self.activate_skill()
        if direction != -1:
            if self.check_if_can_move(direction):
                new_position = self.compute_new_position(direction)
                if self.is_collision(new_position):
                    self.collision(new_position)
                else:
                    self.move(new_position)
        if self.cooldown > 0:
            self.cooldown -= 1
