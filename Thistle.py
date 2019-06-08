from Plant import Plant


class Thistle(Plant):

    def __init__(self, world, position):
        super().__init__(world, position, 'yellow', 'Thistle')
        self.species = 'Thistle'
        self.color = 'yellow'

    def action(self):
        for x in range(3):
            super().action()
