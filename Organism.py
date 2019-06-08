from copy import copy
from Position import Position
from abc import ABC, abstractmethod
from random import randint


class Organism(ABC):

    global_id = 0

    def __init__(self, world, position, color, type, species, initiative=0, strength=0, cooldown=-1, step=1):
        self.id = Organism.id
        Organism.global_id += 1
        self.world = world
        self.position = position
        self.color = color
        self.type = type
        self.initiative = initiative
        self.species = species
        self.strength = strength
        self.cooldown = cooldown
        self.step = step
        self.is_dead = False

    @property
    def initiative(self):
        return self._initiative

    @initiative.setter
    def initiative(self, initiative):
        self._initiative = initiative

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, identificator):
        self._id = identificator

    @property
    def world(self):
        return self._world

    @world.setter
    def world(self, world):
        self._world = world
        
    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, species):
        self._species = species
        
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position
        
    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        self._strength = strength
        
    @property
    def is_dead(self):
        return self._is_dead

    @is_dead.setter
    def is_dead(self, value):
        self._is_dead = value

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, step):
        self._step = step

    @property
    def cooldown(self):
        return self._cooldown

    @cooldown.setter
    def cooldown(self, cooldown):
        self._cooldown = cooldown

    @abstractmethod
    def react_on_collision(self, attacker):
        pass

    @abstractmethod
    def collision(self, position):
        pass

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def multiply(self, partner):
        pass

    def move(self, new_position):
        self.delete_organism_from_board()
        self.place_on_new_position(new_position)
        self.add_organism_on_board()

    def add_organism_on_board(self):
        self.world.add_organism_on_board(self)

    def place_on_new_position(self, position):
        self.position = position

    def delete_organism_from_board(self):
        self.world.delete_organism_from_board(self)

    def get_organism_on_board(self, position):
        return self.world.get_organism_on_board(position)

    def die(self):
        self.is_dead = True
        self.delete_organism_from_board()

    def randomize_direction(self):
        return randint(0, 3)

    def get_world_size(self):
        return self.world.size

    def compute_new_position(self, direction, step=1):
        organism_position = copy(self.position)
        if direction == 0:
            organism_position.y -= step
        if direction == 1:
            organism_position.x += step
        if direction == 2:
            organism_position.y += step
        if direction == 3:
            organism_position.x -= step
        return organism_position

    def check_if_field_occupied(self, position):
        return self.world.check_if_field_occupied(position)

    def is_collision(self, position):
        return self.check_if_field_occupied(position)

    def check_if_can_move(self, direction, step=1):
        organism_position = self.position
        can_move = True
        if direction == 0:
            can_move = Position.check_if_valid(organism_position.y - step)
        if direction == 1:
            can_move = Position.check_if_valid(organism_position.x + step)
        if direction == 2:
            can_move = Position.check_if_valid(organism_position.y + step)
        if direction == 3:
            can_move = Position.check_if_valid(organism_position.x - step)
        return can_move

    def check_if_coordinates_are_valid(self, position):
        return position.check_if_valid(position.x) and position.check_if_valid(position.y)

    def look_for_neighboring_free_field(self):
        organism_position = self.position
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                position = Position(organism_position.x + dx, organism_position.y + dy)
                if self.check_if_coordinates_are_valid(position):
                    if not self.check_if_field_occupied(position):
                        return Position(organism_position.x + dx, organism_position.y + dy)
        return None

    def add_message_to_log(self, message):
            self.world.add_message_to_log(message)

    def prepare_for_save(self):
        save_string = ''
        save_string += self.species + ' '
        save_string += str(self.position.x) + ' ' + str(self.position.y) + ' '
        save_string += str(self.strength) + ' '
        save_string += str(self.cooldown) + '\n'
        return save_string

    @classmethod
    def copy(cls, world, position):
        return cls(world, position)
