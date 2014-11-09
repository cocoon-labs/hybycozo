from face import Face

BOTTOM = 0
TOP = 1


class Hexagon(Face):
    
    def __init__(self, row, vertices):
        super(Hexagon, self).__init__(vertices)
        self._row = row

    @property
    def row(self):
        return self._row
