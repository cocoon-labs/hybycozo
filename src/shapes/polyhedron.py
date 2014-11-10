import opc, time
from vertex import Vertex
from wheel import ColorWheel

DIFFS = [19, 5, 7, 17]
MAX_COLOR = 256


def n0(idx):
    return (idx - 1) % 24
        
def n1(idx):
    return (idx + 1) % 24
        
def n2(idx):
    return (idx - DIFFS[idx % 4]) % 24


class Polyhedron(object):

    vertices = [Vertex(i, {n0(i),n1(i),n2(i)}) for i in xrange(0, 24)]

    def __init__(self, delay=.05, host='localhost', port=7890):
        self.client = opc.Client('{}:{}'.format(host, port))
        self.wheel = ColorWheel()
        self.delay = delay
        self.wheel_pos = 0
 
    def increment_wheel_pos(self, step_size):
        self.wheel_pos = (self.wheel_pos + step_size) % MAX_COLOR

    def update(self):
        frame = [(v.red, v.green, v.blue) for v in self.vertices]
        self.client.put_pixels(frame)
        time.sleep(self.delay)

    def set_all(self, color):
        for v in self.vertices:
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
