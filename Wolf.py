from Animal import Animal


class Wolf(Animal):

    def __init__(self, world, position, strength=9):
        super().__init__(world, position, 'gray55', 'Wolf', 5, strength, -1, 1)
