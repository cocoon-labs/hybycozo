from shapes import TruncatedOctahedron
import time


def test_faces(face_list):
    for face in face_list:
        face.set_all(150, 150, 150)
        trunc_oct.update()
        time.sleep(10)
        face.set_all(0, 0, 0)
    trunc_oct.update()

if __name__ == "__main__":

    trunc_oct = TruncatedOctahedron()

    # raw_input("Ready to test squares...")
    # test_faces(trunc_oct.squares)

    raw_input("Ready to test hexagons...")
    test_faces(trunc_oct.hexagons)
