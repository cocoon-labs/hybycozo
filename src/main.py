from shapes import TruncatedOctahedron
import time


def test_faces(face_list):
    for face in face_list:
        face.set_all((150, 150, 150))
        trunc_oct.update()
        time.sleep(10)
        face.set_all(0, 0, 0)
    trunc_oct.update()

def test_face_positions(trunc_oct, vertex_idx, shape):
    faces = getattr(trunc_oct, shape)
    trunc_oct.set_all((0, 0, 0))
    trunc_oct.update()
    for face in faces:
        face.set_vertex(vertex_idx, trunc_oct.wheel.get_color('rainbow', trunc_oct.wheel_pos))
    trunc_oct.update()
    trunc_oct.increment_wheel_pos(20)
        
    # for i in xrange(0, 6):
    #     trunc_oct.set_all((0, 0, 0))
    #     trunc_oct.update()
    #     for hexagon in trunc_oct.hexagons:
    #         hexagon.set_vertex(i, trunc_oct.wheel.get_color('rainbow', trunc_oct.wheel_pos))
    #     trunc_oct.update()
    #     time.delay(60)
    #     trunc_oct.increment_wheel_pos(20)
        

if __name__ == "__main__":

    trunc_oct = TruncatedOctahedron()

    # raw_input("Ready to test squares...")
    # test_faces(trunc_oct.squares)

    # raw_input("Ready to test hexagons...")
    # test_faces(trunc_oct.hexagons)

    # test_face_positions(trunc_oct, 5, 'hexagons')
    trunc_oct.randomize()
    trunc_oct.run()
    
    # trunc_oct.gradient_cycle('orpal')
