from Organism import Organism
from Position import Position
from random import randint
from SosnowskyBorscht import SosnowskyBorscht
from Antelope import Antelope
from CyberSheep import CyberSheep
from Fox import Fox
from Grass import Grass
from Guarana import Guarana
from Sheep import Sheep
from Thistle import Thistle
from Turtle import Turtle
from Wolf import Wolf
from WolfBerries import WolfBerries
from Human import Human


class World(object):

    def __init__(self, screen):
        self.is_player_on_board = False
        self.is_simulation = False
        self.human = None
        self.screen = screen
        self.board = []
        self.empty_game()
        self.organism_queue = []
        self.size = 20

    @property
    def human(self):
        return self._human

    @human.setter
    def human(self, human):
        self._human = human

    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, screen):
        self._screen = screen

    @property
    def is_player_on_board(self):
        return self._is_player_on_board

    @is_player_on_board.setter
    def is_player_on_board(self, boolean_value):
        self._is_player_on_board = boolean_value

    @property
    def is_simulation(self):
        return self._is_simulation

    @is_simulation.setter
    def is_simulation(self, boolean_value):
        self._is_simulation = boolean_value

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, arr):
        self._board = arr

    @property
    def organism_queue(self):
        return self._organism_queue

    @organism_queue.setter
    def organism_queue(self, queue):
        self._organism_queue = queue

    def save_game(self, file_name):
        with open(file_name, 'w') as output_file:
            for organism in self.organism_queue:
                output_file.write(organism.prepare_for_save())

    def load_game(self, file_name):
        self.empty_game()
        with open(file_name, 'r') as input_file:
            for line in input_file:
                line = line.split()
                self.load_organism(line[0], int(line[1]), int(line[2]), int(line[3]), int(line[4]))

    def draw_empty_board(self):
        for y in range(20):
            for x in range(20):
                position = Position(x, y)
                self.screen.draw_organism(position, 'white')

    def empty_game(self):
        self.organism_queue = []
        self.board = []
        for y in range(20):
            board_list = []
            for x in range(20):
                board_list.append(None)
            self.board.append(board_list)
        self.draw_empty_board()

    def fill_world(self):
        for y in range(20):
            for x in range(20):
                organism_creator = randint(1, 50)
                if organism_creator > 25:
                    self.create_organism(organism_creator, x, y)
                elif not self.is_simulation and not self.is_player_on_board:
                    self.create_human(Position(x, y))

    def add_organism_to_world(self, organism):
        self.add_organism_on_board(organism)
        self.organism_queue.append(organism)

    def create_human(self, position, strength=4, cooldown=0):
        self.is_player_on_board = True
        human = Human(self, position, strength, cooldown)
        self.add_organism_to_world(human)
        self.human = human
        self.update_labels()

    def load_organism(self, organism_species, x, y, strength, cooldown=-1):
        organism_position = Position(x, y)
        if organism_species == "Antelope":
            self.add_organism_to_world(Antelope(self, organism_position, strength))
        if organism_species == "SosnowskyBorscht":
            self.add_organism_to_world(SosnowskyBorscht(self, organism_position))
        if organism_species == "Guarana":
            self.add_organism_to_world(Guarana(self, organism_position))
        if organism_species == "Fox":
            self.add_organism_to_world(Fox(self, organism_position, strength))
        if organism_species == "Thistle":
            self.add_organism_to_world(Thistle(self, organism_position))
        if organism_species == "Sheep":
            self.add_organism_to_world(Sheep(self, organism_position, strength))
        if organism_species == "Grass":
            self.add_organism_to_world(Grass(self, organism_position))
        if organism_species == "WolfBerries":
            self.add_organism_to_world(WolfBerries(self, organism_position))
        if organism_species == "Wolf":
            self.add_organism_to_world(Wolf(self, organism_position, strength))
        if organism_species == "Turtle":
            self.add_organism_to_world(Turtle(self, organism_position, strength))
        if organism_species == "CyberSheep":
            self.add_organism_to_world(CyberSheep(self, organism_position, strength))
        if organism_species == "Human":
            self.create_human(organism_position, strength, cooldown)

    def create_organism_by_name(self, organism_species, x, y, cooldown=-1):
        organism_position = Position(x, y)
        if organism_species == "Antelope":
            self.add_organism_to_world(Antelope(self, organism_position))
        if organism_species == "SosnowskyBorscht":
            self.add_organism_to_world(SosnowskyBorscht(self, organism_position))
        if organism_species == "Guarana":
            self.add_organism_to_world(Guarana(self, organism_position))
        if organism_species == "Fox":
            self.add_organism_to_world(Fox(self, organism_position))
        if organism_species == "Thistle":
            self.add_organism_to_world(Thistle(self, organism_position))
        if organism_species == "Sheep":
            self.add_organism_to_world(Sheep(self, organism_position))
        if organism_species == "Grass":
            self.add_organism_to_world(Grass(self, organism_position))
        if organism_species == "WolfBerries":
            self.add_organism_to_world(WolfBerries(self, organism_position))
        if organism_species == "Wolf":
            self.add_organism_to_world(Wolf(self, organism_position))
        if organism_species == "Turtle":
            self.add_organism_to_world(Turtle(self, organism_position))
        if organism_species == "CyberSheep":
            self.add_organism_to_world(CyberSheep(self, organism_position))
        if organism_species == "Human":
            self.create_human(organism_position, cooldown)

    def create_organism(self, organism_creator, x, y):
        organism_position = Position(x, y)
        if 50 - organism_creator < 2:
            self.add_organism_to_world(Antelope(self, organism_position))
        elif 50 - organism_creator < 4:
            self.add_organism_to_world(SosnowskyBorscht(self, organism_position))
        elif 50 - organism_creator < 6:
            self.add_organism_to_world(Guarana(self, organism_position))
        elif 50 - organism_creator < 8:
            self.add_organism_to_world(Fox(self, organism_position))
        elif 50 - organism_creator < 9:
            self.add_organism_to_world(Thistle(self, organism_position))
        elif 50 - organism_creator < 13:
            self.add_organism_to_world(Sheep(self, organism_position))
        elif 50 - organism_creator < 17:
            self.add_organism_to_world(Grass(self, organism_position))
        elif 50 - organism_creator < 19:
            self.add_organism_to_world(WolfBerries(self, organism_position))
        elif 50 - organism_creator < 22:
            self.add_organism_to_world(Wolf(self, organism_position))
        elif 50 - organism_creator < 24:
            self.add_organism_to_world(Turtle(self, organism_position))
        elif 50 - organism_creator < 25:
            self.add_organism_to_world(CyberSheep(self, organism_position))

    def delete_organism_from_board(self, organism):
        organism_position = organism.position
        self.board[organism_position.y][organism_position.x] = None
        self.screen.draw_organism(organism_position, 'white')

    def destroy_organism(self, organism):
        self.organism_queue.remove(organism)

    def add_organism_on_board(self, organism):
        organism_position = organism.position
        self.board[organism_position.y][organism_position.x] = organism
        self.screen.draw_organism(organism_position, organism.color)

    def check_if_field_occupied(self, position):
        is_occupied = False
        if isinstance(self.board[position.y][position.x], Organism):
            is_occupied = True
        return is_occupied

    def get_organism_on_board(self, position):
        return self.board[position.y][position.x]

    def sort_organism_queue(self):
        self.organism_queue.sort(key=lambda org: org.initiative)

    def perform_round(self):
        self.sort_organism_queue()
        for organism in self.organism_queue:
            if organism is not None:
                if organism.is_dead:
                    self.destroy_organism(organism)
                else:
                    organism.action()
        self.sort_organism_queue()
        self.update_labels()

    def update_labels(self):
        self.screen.set_coords(self.human.position)
        self.screen.set_str(self.human.strength)
        self.screen.set_cooldown(self.human.cooldown)

    def add_message_to_log(self, message):
        self.screen.add_message_to_log(message)

    def print_array(self):
        for y in range(20):
            for x in range(20):
                if isinstance(self.board[y][x], Organism):
                    print('|' + self.board[y][x].species[0] + '|', end='')
                else:
                    print('| |', end='')
            print('\n')
