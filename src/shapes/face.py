

class Face(object):

    def __init__(self, vertices):
        self._vertices = vertices
        self._vertex_set = set(self._vertices)

    @property
    def vertex_set(self):
        return self._vertex_set

    @property
    def vertices(self):
        return self._vertices

    def set_all(self, color):
        for v in self._vertices:
            self._set_vertex_color(v, color)
        
    def set_vertex(self, idx, color):
        v = self.vertices[idx]
        self._set_vertex_color(v, color)

    def _set_vertex_color(self, vertex, color):
        vertex.red = color[0]
        vertex.green = color[1]
        vertex.blue = color[2]
        
            
