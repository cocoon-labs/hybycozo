from vertex import Vertex
from square import Square, HORIZONTAL, VERTICAL
from hexagon import Hexagon, BOTTOM, TOP
from polyhedron import Polyhedron

DIFFS = [19, 5, 7, 17]

def n0(idx):
    return (idx - 1) % 24
        
def n1(idx):
    return (idx + 1) % 24
        
def n2(idx):
    return (idx - DIFFS[idx % 4]) % 24

class TruncatedOctahedron(Polyhedron):
    
    vertices = [Vertex(i, {n0(i),n1(i),n2(i)}) for i in xrange(0, 24)]
    squares = [
        Square(VERTICAL, [vertices[i] for i in [1, 20, 19, 2]]),
        Square(VERTICAL, [vertices[i] for i in [4, 3, 10, 9]]),
        Square(VERTICAL, [vertices[i] for i in [7, 8, 13, 14]]),
        Square(VERTICAL, [vertices[i] for i in [22, 15, 16, 21]]),
        Square(HORIZONTAL, [vertices[i] for i in [0, 5, 6, 23]]),
        Square(HORIZONTAL, [vertices[i] for i in [18, 11, 12, 17]])
    ]
    hexagons = [
        Hexagon(BOTTOM, [vertices[i] for i in [0, 1, 2, 3, 4, 5]]),
        Hexagon(BOTTOM, [vertices[i] for i in [5, 4, 9, 8, 7, 6]]),
        Hexagon(BOTTOM, [vertices[i] for i in [6, 7, 14, 15, 22, 23]]),
        Hexagon(BOTTOM, [vertices[i] for i in [23, 22, 21, 20, 1, 0]]),
        Hexagon(TOP, [vertices[i] for i in [2, 19, 18, 11, 10, 3]]),
        Hexagon(TOP, [vertices[i] for i in [9, 10, 11, 12, 13, 8]]),
        Hexagon(TOP, [vertices[i] for i in [14, 13, 12, 17, 16, 15]]),
        Hexagon(TOP, [vertices[i] for i in [21, 16, 17, 18, 19, 20]])
    ]
