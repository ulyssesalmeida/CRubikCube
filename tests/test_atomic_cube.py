import sys
import unittest

sys.path.append("./src/")

from AtomicCube import AtomicCube

class AtomicCubeTestCase(unittest.TestCase):
    def setUp(self):
        self.atomic_cube = AtomicCube()

    def test_initial_state(self):
        self.assertEqual(self.atomic_cube.upper_face, "YL")
        self.assertEqual(self.atomic_cube.down_face, "WT")
        self.assertEqual(self.atomic_cube.front_face, "BL")
        self.assertEqual(self.atomic_cube.back_face, "GR")
        self.assertEqual(self.atomic_cube.right_face, "RD")
        self.assertEqual(self.atomic_cube.left_face, "ON")

    def test_up_rotate(self):
        self.atomic_cube.up_rotate()
        self.assertEqual(self.atomic_cube.upper_face, "YL")
        self.assertEqual(self.atomic_cube.down_face, "WT")
        self.assertEqual(self.atomic_cube.front_face, "RD")
        self.assertEqual(self.atomic_cube.back_face, "ON")
        self.assertEqual(self.atomic_cube.right_face, "GR")
        self.assertEqual(self.atomic_cube.left_face, "BL")

    def test_up_rotate_anticlockwise(self):
        self.atomic_cube.up_rotate(clockwise=False)
        self.assertEqual(self.atomic_cube.upper_face, "YL")
        self.assertEqual(self.atomic_cube.down_face, "WT")
        self.assertEqual(self.atomic_cube.front_face, "ON")
        self.assertEqual(self.atomic_cube.back_face, "RD")
        self.assertEqual(self.atomic_cube.right_face, "BL")
        self.assertEqual(self.atomic_cube.left_face, "GR")

    def test_down_rotate(self):
        self.atomic_cube.down_rotate()
        self.assertEqual(self.atomic_cube.upper_face, "YL")
        self.assertEqual(self.atomic_cube.down_face, "WT")
        self.assertEqual(self.atomic_cube.front_face, "ON")
        self.assertEqual(self.atomic_cube.back_face, "RD")
        self.assertEqual(self.atomic_cube.right_face, "BL")
        self.assertEqual(self.atomic_cube.left_face, "GR")

    def test_down_rotate_anticlockwise(self):
        self.atomic_cube.down_rotate(clockwise=False)
        self.assertEqual(self.atomic_cube.upper_face, "YL")
        self.assertEqual(self.atomic_cube.down_face, "WT")
        self.assertEqual(self.atomic_cube.front_face, "RD")
        self.assertEqual(self.atomic_cube.back_face, "ON")
        self.assertEqual(self.atomic_cube.right_face, "GR")
        self.assertEqual(self.atomic_cube.left_face, "BL")

    def test_front_rotate(self):
        self.atomic_cube.front_rotate()
        self.assertEqual(self.atomic_cube.upper_face, "ON")
        self.assertEqual(self.atomic_cube.down_face, "RD")
        self.assertEqual(self.atomic_cube.front_face, "BL")
        self.assertEqual(self.atomic_cube.back_face, "GR")
        self.assertEqual(self.atomic_cube.right_face, "YL")
        self.assertEqual(self.atomic_cube.left_face, "WT")

    def test_front_rotate_anticlockwise(self):
        self.atomic_cube.front_rotate(clockwise=False)
        self.assertEqual(self.atomic_cube.upper_face, "RD")
        self.assertEqual(self.atomic_cube.down_face, "ON")
        self.assertEqual(self.atomic_cube.front_face, "BL")
        self.assertEqual(self.atomic_cube.back_face, "GR")
        self.assertEqual(self.atomic_cube.right_face, "WT")
        self.assertEqual(self.atomic_cube.left_face, "YL")

    def test_back_rotate(self):
        self.atomic_cube.back_rotate()
        self.assertEqual(self.atomic_cube.upper_face, "RD")
        self.assertEqual(self.atomic_cube.down_face, "ON")
        self.assertEqual(self.atomic_cube.front_face, "BL")
        self.assertEqual(self.atomic_cube.back_face, "GR")
        self.assertEqual(self.atomic_cube.right_face, "WT")
        self.assertEqual(self.atomic_cube.left_face, "YL")

    def test_back_rotate_anticlockwise(self):
        self.atomic_cube.back_rotate(clockwise=False)
        self.assertEqual(self.atomic_cube.upper_face, "ON")
        self.assertEqual(self.atomic_cube.down_face, "RD")
        self.assertEqual(self.atomic_cube.front_face, "BL")
        self.assertEqual(self.atomic_cube.back_face, "GR")
        self.assertEqual(self.atomic_cube.right_face, "YL")
        self.assertEqual(self.atomic_cube.left_face, "WT")

    def test_right_rotate(self):
        self.atomic_cube.right_rotate()
        self.assertEqual(self.atomic_cube.upper_face, "BL")
        self.assertEqual(self.atomic_cube.down_face, "GR")
        self.assertEqual(self.atomic_cube.front_face, "WT")
        self.assertEqual(self.atomic_cube.back_face, "YL")
        self.assertEqual(self.atomic_cube.right_face, "RD")
        self.assertEqual(self.atomic_cube.left_face, "ON")

    def test_right_rotate_anticlockwise(self):
        self.atomic_cube.right_rotate(clockwise=False)
        self.assertEqual(self.atomic_cube.upper_face, "GR")
        self.assertEqual(self.atomic_cube.down_face, "BL")
        self.assertEqual(self.atomic_cube.front_face, "YL")
        self.assertEqual(self.atomic_cube.back_face, "WT")
        self.assertEqual(self.atomic_cube.right_face, "RD")
        self.assertEqual(self.atomic_cube.left_face, "ON")

    def test_left_rotate(self):
        self.atomic_cube.left_rotate()
        self.assertEqual(self.atomic_cube.upper_face, "GR")
        self.assertEqual(self.atomic_cube.down_face, "BL")
        self.assertEqual(self.atomic_cube.front_face, "YL")
        self.assertEqual(self.atomic_cube.back_face, "WT")
        self.assertEqual(self.atomic_cube.right_face, "RD")
        self.assertEqual(self.atomic_cube.left_face, "ON")

    def test_left_rotate_anticlockwise(self):
        self.atomic_cube.left_rotate(clockwise=False)
        self.assertEqual(self.atomic_cube.upper_face, "BL")
        self.assertEqual(self.atomic_cube.down_face, "GR")
        self.assertEqual(self.atomic_cube.front_face, "WT")
        self.assertEqual(self.atomic_cube.back_face, "YL")
        self.assertEqual(self.atomic_cube.right_face, "RD")
        self.assertEqual(self.atomic_cube.left_face, "ON")

    def test_repr(self):
        cube_repr = """   |GR|
   |YL|
|ON|BL|RD|
   |WT|"""
        self.assertEqual(repr(self.atomic_cube), cube_repr)

    def test_show_face(self):
        self.assertEqual(self.atomic_cube.show_face("U"),"YL")
        self.assertEqual(self.atomic_cube.show_face("D"),"WT")
        self.assertEqual(self.atomic_cube.show_face("F"),"BL")
        self.assertEqual(self.atomic_cube.show_face("B"),"GR")
        self.assertEqual(self.atomic_cube.show_face("R"),"RD")
        self.assertEqual(self.atomic_cube.show_face("L"),"ON")

    def test_comparison(self):
        second_cube = AtomicCube()
        self.assertEqual(self.atomic_cube, second_cube)
        second_cube.up_rotate()
        self.assertNotEqual(self.atomic_cube, second_cube)
        second_cube.up_rotate()
        second_cube.up_rotate()
        second_cube.up_rotate()
        self.assertEqual(self.atomic_cube, second_cube)
