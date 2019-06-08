from tkinter import *
from tkinter import filedialog
from Position import Position
from World import World
from tkinter.scrolledtext import ScrolledText


class Screen:

    def __init__(self):
        self.rect_size = 30
        self.main_window = Tk()
        self.main_window.title("175489 Krzysztof Zajaczkowski")
        self.main_window.bind("<KeyPress>", self.keydown)
        self.main_window.focus_set()
        self.top_frame = Frame(self.main_window)
        self.top_frame.pack()
        self.middle_frame = Frame(self.main_window)
        self.middle_frame.pack()
        self.bottom_frame = Frame(self.main_window)
        self.bottom_frame.pack(side=BOTTOM)
        self.human_coords = StringVar()
        self.human_coords_label = Label(self.top_frame, textvariable=self.human_coords)
        self.human_str = StringVar()
        self.human_str_label = Label(self.top_frame, textvariable=self.human_str)
        self.human_cooldown = StringVar()
        self.human_cooldown_label = Label(self.top_frame, textvariable=self.human_cooldown)
        self.human_action = None
        self.human_action_string = StringVar()
        self.human_action_label = Label(self.top_frame, textvariable=self.human_action_string)
        self.save_button = Button(self.bottom_frame, text="Save Game", command=self.save_game)
        self.load_button = Button(self.bottom_frame, text="Load Game", command=self.load_game)
        self.canvas = Canvas(self.middle_frame, width=20*self.rect_size+10, height=20*self.rect_size+10)
        self.log = ScrolledText(master=self.bottom_frame, wrap=WORD, width=40, height=5)
        self.log.tag_config('human', background='yellow', foreground='red')
        self.log.config(state=DISABLED)
        self.log.pack(side=RIGHT)
        self.canvas.pack()
        self.print_board()
        self.human_coords_label.pack(side=LEFT)
        self.human_str_label.pack(side=LEFT)
        self.human_cooldown_label.pack(side=LEFT)
        self.human_action_label.pack(side=LEFT)
        self.save_button.pack(side=LEFT)
        self.load_button.pack(side=LEFT)
        self.world = World(self)

    @property
    def world(self):
        return self._world

    @world.setter
    def world(self, world):
        self._world = world
        
    @property
    def human_action(self):
        return self._human_action

    @human_action.setter
    def human_action(self, action):
        self._human_action = action

    def keydown(self, e):
        if e.keycode == 38:
            self.world.human.chosen_action = 'Up'
            self.set_action_string('Up')
        elif e.keycode == 39:
            self.world.human.chosen_action = 'Right'
            self.set_action_string('Right')
        elif e.keycode == 40:
            self.world.human.chosen_action = 'Down'
            self.set_action_string('Down')
        elif e.keycode == 37:
            self.world.human.chosen_action = 'Left'
            self.set_action_string('Left')
        else:
            if e.char == 'r' or e.char == 'R':
                self.world.human.chosen_action = 'Skill'
                self.set_action_string('Activate skill')
            if e.char == ' ':
                self.world.perform_round()

    def print_board(self):
        for y in range(20):
            for x in range(20):
                self.draw_organism(Position(x, y), 'white')

    def perform_round(self):
        self.world.perform_round()

    def set_action_string(self, action):
        self.human_action_string.set('Action: ' + action)

    def set_coords(self, position):
        self.human_coords.set("X: " + str(position.x) + " Y: " + str(position.y))

    def set_str(self, strength):
        self.human_str.set("Str: " + str(strength))

    def set_cooldown(self, cooldown):
        self.human_cooldown.set("CD: " + str(cooldown))

    def change_label(self, label, string):
        label.config(text=string)

    def add_message_to_log(self, message):
        self.log.config(state=NORMAL)
        if 'Human' in message:
            self.log.insert(INSERT, message + '\n', 'human')
        else:
            self.log.insert(INSERT, message + '\n')
        self.log.config(state=DISABLED)
        self.log.see('end')

    def draw_organism(self, position, color):
        drawing_start_x = 5+position.x*30
        drawing_start_y = 5+position.y*30
        self.canvas.create_rectangle(drawing_start_x, drawing_start_y, drawing_start_x + self.rect_size,
                                     drawing_start_y + self.rect_size, fill=color)

    def save_game(self):
        file_name = filedialog.asksaveasfilename(defaultextension=".txt", initialdir="/", title="Select file",
                                                 filetypes=(("Text file", "*.txt"), ("All Files", "*.*")))
        if file_name is not None:
            self.world.save_game(file_name)

    def load_game(self):
        file_name = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("Text file", "*.txt"), ("All Files", "*.*")))
        if file_name is not None:
            self.world.load_game(file_name)

    def show(self):
        self.main_window.mainloop()
