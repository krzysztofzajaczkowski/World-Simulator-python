
class Position(object):

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x_position):
        self._x = x_position

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y_position):
        self._y = y_position

    @classmethod
    def check_if_valid(cls, coordinate):
        return 0 <= coordinate < 20

    def is_valid(self):
        return 0 <= self.x < 20 and 0 <= self.y < 20
