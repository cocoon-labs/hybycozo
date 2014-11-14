import opc, time
from vertex import Vertex
from wheel import ColorWheel, SCHEMES
from random import randrange, random

DIFFS = [19, 5, 7, 17]
MAX_COLOR = 256
MAX_COLOR_STEP = 30
MAX_FADEFACTOR = 10


def n0(idx):
    return (idx - 1) % 24
        
def n1(idx):
    return (idx + 1) % 24
        
def n2(idx):
    return (idx - DIFFS[idx % 4]) % 24


class Polyhedron(object):

    vertices = [Vertex(i, {n0(i),n1(i),n2(i)}) for i in xrange(0, 24)]
    available_schemes = SCHEMES.keys()

    def __init__(self, delay=.05, host='localhost', port=7890):
        self.client = opc.Client('{}:{}'.format(host, port))
        self.wheel = ColorWheel()
        self._update_delay = delay
        self.wheel_pos = 0
        self._functions = []
        self._step_fn = None
        self._switch_prob = 100
        self.gradient = 'cool'
        self._gradient_prob = 100
        self.color_step = 1
        self._color_prob = 100
        self.fade_factor = 2
        self._fadefactor_prob = 100
        self.step_delay = .15
        self._step_delay_prob = 100


    def run(self):
        while True:
            self.randomize()
            self._step_fn()

    def randomize(self):
        if not randrange(0, self._switch_prob):
            self._switch_fn()
        if not randrange(0, self._gradient_prob):
            self._switch_gradient()
        if not randrange(0, self._color_prob):
            self.color_step = 1 + randrange(0, MAX_COLOR_STEP)
        if not randrange(0, self._fadefactor_prob):
            self.fade_factor = 2 + randrange(0, MAX_FADEFACTOR)
        if not randrange(0, self._step_delay_prob):
            self.step_delay = 0.05 + (0.15 * random())

    def _switch_fn(self):
        fn_idx = randrange(0, len(self._functions))
        self._step_fn = self._functions[fn_idx]
        
    def _switch_gradient(self):
        fn_idx = randrange(0, len(self.available_schemes))
        self.gradient = self.available_schemes[fn_idx]
 
    def increment_wheel_pos(self):
        self.wheel_pos = (self.wheel_pos + self.color_step) % MAX_COLOR

    def update(self):
        frame = [(v.red, v.green, v.blue) for v in self.vertices]
        self.client.put_pixels(frame)
        time.sleep(self._update_delay)

    def set_all(self, color):
        for v in self.vertices:
            v.red = color[0]
            v.green = color[1]
            v.blue = color[2]

    def set_vertex(self, idx, color):
        v = self.vertices[idx]
        v.red = color[0]
        v.green = color[1]
        v.blue = color[2]

    def gradient_cycle(self, scheme, step_size=1):
        while True:
            self.set_all(
                self.wheel.get_color(scheme, self.wheel_pos)
            )
            self.increment_wheel_pos(step_size)
            self.update()
    
    def fade_factory(self, factor=None):
        factor = factor or self.fade_factor
        for v in self.vertices:
            v.red /= factor
            v.green /= factor
            v.blue /= factor
