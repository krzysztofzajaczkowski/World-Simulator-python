from Plant import Plant


class Grass(Plant):

    def __init__(self, world, position):
        super().__init__(world, position, 'forest green', 'Grass', 0)