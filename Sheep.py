from Animal import Animal


class Sheep(Animal):

    def __init__(self, world, position, strength=4):
        super().__init__(world, position, 'gray1', 'Sheep', 4, strength, -1, 1)
