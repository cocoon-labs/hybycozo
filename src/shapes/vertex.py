

class Vertex(object):
    
    def __init__(self, idx, neighbors=set()):
        self.idx = idx
        self.neighbors = neighbors
        self.red = 0
        self.green = 0
        self.blue = 0
        
