from square import Square, HORIZONTAL, VERTICAL
from hexagon import Hexagon, BOTTOM, TOP
from polyhedron import Polyhedron
import time
from random import randrange

CLOCKWISE = -1
COUNTER_CW = 1
MAX_COLOR = 256
MAX_HISTORY = 3
BLACK = (0,0,0)


class TruncatedOctahedron(Polyhedron):
    
    squares = [
        Square(VERTICAL, [Polyhedron.vertices[i] for i in [1, 20, 19, 2]]),
        Square(VERTICAL, [Polyhedron.vertices[i] for i in [4, 3, 10, 9]]),
        Square(VERTICAL, [Polyhedron.vertices[i] for i in [7, 8, 13, 14]]),
        Square(VERTICAL, [Polyhedron.vertices[i] for i in [22, 15, 16, 21]]),
        Square(HORIZONTAL, [Polyhedron.vertices[i] for i in [0, 5, 6, 23]]),
        Square(HORIZONTAL, [Polyhedron.vertices[i] for i in [18, 11, 12, 17]])
    ]
    hexagons = [
        Hexagon(BOTTOM, [Polyhedron.vertices[i] for i in [0, 1, 2, 3, 4, 5]]),
        Hexagon(BOTTOM, [Polyhedron.vertices[i] for i in [5, 4, 9, 8, 7, 6]]),
        Hexagon(BOTTOM, [Polyhedron.vertices[i] for i in [6, 7, 14, 15, 22, 23]]),
        Hexagon(BOTTOM, [Polyhedron.vertices[i] for i in [23, 22, 21, 20, 1, 0]]),
        Hexagon(TOP, [Polyhedron.vertices[i] for i in [2, 19, 18, 11, 10, 3]]),
        Hexagon(TOP, [Polyhedron.vertices[i] for i in [9, 10, 11, 12, 13, 8]]),
        Hexagon(TOP, [Polyhedron.vertices[i] for i in [14, 13, 12, 17, 16, 15]]),
        Hexagon(TOP, [Polyhedron.vertices[i] for i in [21, 16, 17, 18, 19, 20]])
    ]

    def __init__(self, delay=0.5, host='localhost', port=7890):
        super(TruncatedOctahedron, self).__init__(delay, host, port)
        self._functions = [
            self.cycle_vertical_squares,
            self.top_bottom_atmosphere,
            self.sparkle,
            self.shapeshift,
            self.random_walk,
            self.virus,
            self.the_clap
        ]
        self._step_fn = self._functions[0]

        self._cvs_dir = CLOCKWISE
        self._cvs_pos = 0

        self._tb_atm_pos_top = 0
        self._tb_atm_dir_top = CLOCKWISE
        self._tb_atm_pos_bot = 0
        self._tb_atm_dir_bot = CLOCKWISE
        self._dir_change_prob = 25
    
    def cycle_vertical_squares(self):
        self.fade_factory()

        color = self.get_color()
        for square in self.squares:
            square.set_vertex(self._cvs_pos, color)
        
        self.increment_wheel_pos()
        self._cvs_pos = (self._cvs_pos + self._cvs_dir) % 4
        self.update()
        time.sleep(self.step_delay)

    def top_bottom_atmosphere(self):
        self.fade_factory()

        color1 = self.wheel.get_color(self.gradient,
                                      self.wheel_pos)
        bottom = self.squares[4]
        bottom.set_vertex(self._tb_atm_pos_bot, color1)
        self._tb_atm_pos_bot = (self._tb_atm_pos_bot +
                                self._tb_atm_dir_bot) % 4
        

        color2 = self.wheel.get_color(self.gradient,
                                      (self.wheel_pos + 128) % MAX_COLOR)
        top = self.squares[5]
        top.set_vertex(self._tb_atm_pos_top, color2)
        self._tb_atm_pos_top = (self._tb_atm_pos_top +
                                self._tb_atm_dir_top) % 4


        self.increment_wheel_pos()
        self.update()
        time.sleep(self.step_delay)

    def sparkle(self):
        self.fade_factory()
        vert_idx = randrange(0, len(self.vertices))
        color = self.get_color()
        self.set_vertex(vert_idx, color)
        self.increment_wheel_pos()
        self.update()
        time.sleep(0.05)

    def shapeshift(self):
        faces = self.squares + self.hexagons
        face_idx = randrange(0, len(faces))
        the_face = faces[face_idx]
        
        color = self.get_color()
        factor = 20
        while factor > 1:
            the_face.set_all(color)
            self.fade_factory(factor)
            factor -= 2
            self.update()
            time.sleep(self.step_delay)
        
        time.sleep(5)
        for i in xrange(0, 10):
            self.fade_factory(1.2)
            self.update()
            time.sleep(0.1)

        self.increment_wheel_pos()

    def random_walk(self):
        history = []

        curr = randrange(0, len(self.vertices))
        history.append(curr)
       
        while True:
            self.fade_factory()
            color = self.get_color()
            vert = self.vertices[curr]
            self.set_vertex(curr, color)
            options = [n for n in vert.neighbors \
                       if not n in history]
            if not options:
                break

            history.append(options[randrange(0, len(options))])
            if len(history) > MAX_HISTORY:
                history.pop(0)
            curr = history[-1]

            self.increment_wheel_pos()
            self.update()
            time.sleep(self.step_delay)


    def virus(self):
        carrier = randrange(0, len(self.vertices))
        infected = {carrier}
        color = self.get_color()
        prev_n_infected = 0

        while len(infected) > prev_n_infected:
            prev_n_infected = len(infected)
            self.fade_factory()
            [self.set_vertex(v, color) for v in infected]
            for v in infected:
                infected = infected.union(self.vertices[v].neighbors)
            
            self.update()
            time.sleep(self.step_delay)
    
        self.increment_wheel_pos()
        self.fade_factory()

    def the_clap(self):
        carrier = randrange(0, len(self.vertices))
        infected = {carrier}
        color = self.get_color()
        prev_n_infected = 0

        while len(infected) > prev_n_infected:
            prev_n_infected = len(infected)
            self.fade_factory()
            [self.set_vertex(v, color) for v in infected]
            next_infected = set()
            for v in infected:
                neighbs = [n for n in self.vertices[v].neighbors \
                          if n not in infected]
                next_infected = next_infected.union(neighbs)

            infected = next_infected
            
            self.update()
            time.sleep(self.step_delay)
    
        self.increment_wheel_pos()
        self.fade_factory()
            
    def get_color(self):
        return self.wheel.get_color(self.gradient, self.wheel_pos)

    def _randomize_dir(self):
        if not randrange(0, self._dir_change_prob):
            self._cvs_dir *= -1
        if not randrange(0, self._dir_change_prob):
            self._tb_atm_dir_top *= -1
        if not randrange(0, self._dir_change_prob):
            self._tb_atm_dir_bot *= -1

