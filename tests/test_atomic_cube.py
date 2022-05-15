import unittest

from src.AtomicCube import AtomicCube

class AtomicCubeTestCase(unittest.TestCase):
    def setUp(self):
        self.atomic_cube = AtomicCube()

    def test_initial_state(self):
        self.assertEqual (self.atomic_cube.upper_face, "YL")
        self.assertEqual (self.atomic_cube.down_face, "WT")
        self.assertEqual (self.atomic_cube.front_face, "BL")
        self.assertEqual (self.atomic_cube.back_face, "GR")
        self.assertEqual (self.atomic_cube.right_face, "RD")
        self.assertEqual (self.atomic_cube.left_face, "ON")

    def test_up_rotate(self):
        self.atomic_cube.up_rotate()
        self.assertEqual (self.atomic_cube.upper_face, "YL")
        self.assertEqual (self.atomic_cube.down_face, "WT")
        self.assertEqual (self.atomic_cube.front_face, "RD")
        self.assertEqual (self.atomic_cube.back_face, "ON")
        self.assertEqual (self.atomic_cube.right_face, "GR")
        self.assertEqual (self.atomic_cube.left_face, "BL")

    def test_up_rotate_anticlockwise(self):
        self.atomic_cube.up_rotate(clockwise=False)
        self.assertEqual (self.atomic_cube.upper_face, "YL")
        self.assertEqual (self.atomic_cube.down_face, "WT")
        self.assertEqual (self.atomic_cube.front_face, "ON")
        self.assertEqual (self.atomic_cube.back_face, "RD")
        self.assertEqual (self.atomic_cube.right_face, "BL")
        self.assertEqual (self.atomic_cube.left_face, "GR")

    def test_down_rotate(self):
        self.atomic_cube.down_rotate()
        self.assertEqual (self.atomic_cube.upper_face, "YL")
        self.assertEqual (self.atomic_cube.down_face, "WT")
        self.assertEqual (self.atomic_cube.front_face, "ON")
        self.assertEqual (self.atomic_cube.back_face, "RD")
        self.assertEqual (self.atomic_cube.right_face, "BL")
        self.assertEqual (self.atomic_cube.left_face, "GR")

    def test_down_rotate_anticlockwise(self):
        self.atomic_cube.down_rotate(clockwise=False)
        self.assertEqual (self.atomic_cube.upper_face, "YL")
        self.assertEqual (self.atomic_cube.down_face, "WT")
        self.assertEqual (self.atomic_cube.front_face, "RD")
        self.assertEqual (self.atomic_cube.back_face, "ON")
        self.assertEqual (self.atomic_cube.right_face, "GR")
        self.assertEqual (self.atomic_cube.left_face, "BL")

    def test_front_rotate(self):
        self.atomic_cube.front_rotate()
        self.assertEqual (self.atomic_cube.upper_face, "ON")
        self.assertEqual (self.atomic_cube.down_face, "RD")
        self.assertEqual (self.atomic_cube.front_face, "BL")
        self.assertEqual (self.atomic_cube.back_face, "GR")
        self.assertEqual (self.atomic_cube.right_face, "YL")
        self.assertEqual (self.atomic_cube.left_face, "WT")

    def test_front_rotate_anticlockwise(self):
        self.atomic_cube.front_rotate(clockwise=False)
        self.assertEqual (self.atomic_cube.upper_face, "RD")
        self.assertEqual (self.atomic_cube.down_face, "ON")
        self.assertEqual (self.atomic_cube.front_face, "BL")
        self.assertEqual (self.atomic_cube.back_face, "GR")
        self.assertEqual (self.atomic_cube.right_face, "WT")
        self.assertEqual (self.atomic_cube.left_face, "YL")

    def test_back_rotate(self):
        self.atomic_cube.back_rotate()
        self.assertEqual (self.atomic_cube.upper_face, "RD")
        self.assertEqual (self.atomic_cube.down_face, "ON")
        self.assertEqual (self.atomic_cube.front_face, "BL")
        self.assertEqual (self.atomic_cube.back_face, "GR")
        self.assertEqual (self.atomic_cube.right_face, "WT")
        self.assertEqual (self.atomic_cube.left_face, "YL")

    def test_back_rotate_anticlockwise(self):
        self.atomic_cube.back_rotate(clockwise=False)
        self.assertEqual (self.atomic_cube.upper_face, "ON")
        self.assertEqual (self.atomic_cube.down_face, "RD")
        self.assertEqual (self.atomic_cube.front_face, "BL")
        self.assertEqual (self.atomic_cube.back_face, "GR")
        self.assertEqual (self.atomic_cube.right_face, "YL")
        self.assertEqual (self.atomic_cube.left_face, "WT")

    def test_right_rotate(self):
        self.atomic_cube.right_rotate()
        self.assertEqual (self.atomic_cube.upper_face, "BL")
        self.assertEqual (self.atomic_cube.down_face, "GR")
        self.assertEqual (self.atomic_cube.front_face, "WT")
        self.assertEqual (self.atomic_cube.back_face, "YL")
        self.assertEqual (self.atomic_cube.right_face, "RD")
        self.assertEqual (self.atomic_cube.left_face, "ON")

    def test_right_rotate_anticlockwise(self):
        self.atomic_cube.right_rotate(clockwise=False)
        self.assertEqual (self.atomic_cube.upper_face, "GR")
        self.assertEqual (self.atomic_cube.down_face, "BL")
        self.assertEqual (self.atomic_cube.front_face, "YL")
        self.assertEqual (self.atomic_cube.back_face, "WT")
        self.assertEqual (self.atomic_cube.right_face, "RD")
        self.assertEqual (self.atomic_cube.left_face, "ON")

    def test_left_rotate(self):
        self.atomic_cube.left_rotate()
        self.assertEqual (self.atomic_cube.upper_face, "GR")
        self.assertEqual (self.atomic_cube.down_face, "BL")
        self.assertEqual (self.atomic_cube.front_face, "YL")
        self.assertEqual (self.atomic_cube.back_face, "WT")
        self.assertEqual (self.atomic_cube.right_face, "RD")
        self.assertEqual (self.atomic_cube.left_face, "ON")

    def test_left_rotate_anticlockwise(self):
        self.atomic_cube.left_rotate(clockwise=False)
        self.assertEqual (self.atomic_cube.upper_face, "BL")
        self.assertEqual (self.atomic_cube.down_face, "GR")
        self.assertEqual (self.atomic_cube.front_face, "WT")
        self.assertEqual (self.atomic_cube.back_face, "YL")
        self.assertEqual (self.atomic_cube.right_face, "RD")
        self.assertEqual (self.atomic_cube.left_face, "ON")
