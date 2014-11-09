from face import Face

VERTICAL = 0
HORIZONTAL = 1


class Square(Face):
    
    def __init__(self, orientation, vertices):
        super(Square, self).__init__(vertices)
        self._orientation = orientation
        
    @property
    def orientation(self):
        return self._orientation
