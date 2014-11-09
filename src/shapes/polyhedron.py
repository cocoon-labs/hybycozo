import opc, time

class Polyhedron(object):

    def __init__(self, host='localhost', port=7890):
        self.client = opc.Client('{}:{}'.format(host, port))

    def update(self):
        frame = [(v.red, v.green, v.blue) for v in self.vertices]
        self.client.put_pixels(frame)
        time.sleep(0.05)
