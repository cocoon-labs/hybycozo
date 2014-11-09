

class Face(object):

    def __init__(self, vertices):
        self._vertices = vertices
        self._vertex_set = set(self._vertices)

    @property
    def vertex_set(self):
        return self._vertex_set

    @property
    def vertex(self):
        return self._vertices

    def set_all(self, red, green, blue):
        for v in self._vertices:
            v.red = red
            v.green = green
            v.blue = blue
            
