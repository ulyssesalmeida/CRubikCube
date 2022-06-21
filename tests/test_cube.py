import sys
import unittest

sys.path.append("./src/")

from Cube import Cube

class CubeTestCase(unittest.TestCase):
    def setUp(self):
        self.cube = Cube()

    def test_repr(self):
        cube_repr = """         |GR|GR|GR|
         |GR|GR|GR|
         |GR|GR|GR|
         |YL|YL|YL|
         |YL|YL|YL|
         |YL|YL|YL|
|ON|ON|ON|BL|BL|BL|RD|RD|RD|
|ON|ON|ON|BL|BL|BL|RD|RD|RD|
|ON|ON|ON|BL|BL|BL|RD|RD|RD|
         |WT|WT|WT|
         |WT|WT|WT|
         |WT|WT|WT|"""
        self.assertEqual(repr(self.cube),cube_repr)

    def test_print_up_face(self):
        face_repr = """|YL|YL|YL|
|YL|YL|YL|
|YL|YL|YL|"""
        self.assertEqual(self.cube.print_face("U"), face_repr)

    def test_print_down_face(self):
        face_repr = """|WT|WT|WT|
|WT|WT|WT|
|WT|WT|WT|"""
        self.assertEqual(self.cube.print_face("D"), face_repr)

    def test_print_front_face(self):
        face_repr = """|BL|BL|BL|
|BL|BL|BL|
|BL|BL|BL|"""
        self.assertEqual(self.cube.print_face("F"), face_repr)

    def test_print_back_face(self):
        face_repr = """|GR|GR|GR|
|GR|GR|GR|
|GR|GR|GR|"""
        self.assertEqual(self.cube.print_face("B"), face_repr)

    def test_print_right_face(self):
        face_repr = """|RD|RD|RD|
|RD|RD|RD|
|RD|RD|RD|"""
        self.assertEqual(self.cube.print_face("R"), face_repr)

    def test_print_left_face(self):
        face_repr = """|ON|ON|ON|
|ON|ON|ON|
|ON|ON|ON|"""
        self.assertEqual(self.cube.print_face("L"), face_repr)

class CubeRotationsTestCase(unittest.TestCase):
    def setUp(self):
        self.cube = Cube()

    def test_up_rotate(self):
        cube_repr = """         |GR|GR|GR|
         |GR|GR|GR|
         |ON|ON|ON|
         |YL|YL|YL|
         |YL|YL|YL|
         |YL|YL|YL|
|BL|BL|BL|RD|RD|RD|GR|GR|GR|
|ON|ON|ON|BL|BL|BL|RD|RD|RD|
|ON|ON|ON|BL|BL|BL|RD|RD|RD|
         |WT|WT|WT|
         |WT|WT|WT|
         |WT|WT|WT|"""
        self.cube.up_rotate()
        self.assertEqual(repr(self.cube),cube_repr)

    def test_up_rotate_anti_clockwise(self):
        cube_repr = """         |GR|GR|GR|
         |GR|GR|GR|
         |RD|RD|RD|
         |YL|YL|YL|
         |YL|YL|YL|
         |YL|YL|YL|
|GR|GR|GR|ON|ON|ON|BL|BL|BL|
|ON|ON|ON|BL|BL|BL|RD|RD|RD|
|ON|ON|ON|BL|BL|BL|RD|RD|RD|
         |WT|WT|WT|
         |WT|WT|WT|
         |WT|WT|WT|"""
        self.cube.up_rotate(clockwise=False)
        self.assertEqual(repr(self.cube),cube_repr)

    def test_right_rotate(self):
        cube_repr = """         |GR|GR|YL|
         |GR|GR|YL|
         |GR|GR|YL|
         |YL|YL|BL|
         |YL|YL|BL|
         |YL|YL|BL|
|ON|ON|ON|BL|BL|WT|RD|RD|RD|
|ON|ON|ON|BL|BL|WT|RD|RD|RD|
|ON|ON|ON|BL|BL|WT|RD|RD|RD|
         |WT|WT|GR|
         |WT|WT|GR|
         |WT|WT|GR|"""
        self.cube.right_rotate()
        self.assertEqual(repr(self.cube),cube_repr)

    def test_left_rotate(self):
        cube_repr = """         |WT|GR|GR|
         |WT|GR|GR|
         |WT|GR|GR|
         |GR|YL|YL|
         |GR|YL|YL|
         |GR|YL|YL|
|ON|ON|ON|YL|BL|BL|RD|RD|RD|
|ON|ON|ON|YL|BL|BL|RD|RD|RD|
|ON|ON|ON|YL|BL|BL|RD|RD|RD|
         |BL|WT|WT|
         |BL|WT|WT|
         |BL|WT|WT|"""
        self.cube.left_rotate()
        self.assertEqual(repr(self.cube),cube_repr)

    def test_front_rotate(self):
        cube_repr = """         |GR|GR|GR|
         |GR|GR|GR|
         |GR|GR|GR|
         |YL|YL|YL|
         |YL|YL|YL|
         |ON|ON|ON|
|ON|ON|WT|BL|BL|BL|YL|RD|RD|
|ON|ON|WT|BL|BL|BL|YL|RD|RD|
|ON|ON|WT|BL|BL|BL|YL|RD|RD|
         |RD|RD|RD|
         |WT|WT|WT|
         |WT|WT|WT|"""
        self.cube.front_rotate()
        self.assertEqual(repr(self.cube),cube_repr)

    def test_back_rotate(self):
        cube_repr = """         |GR|GR|GR|
         |GR|GR|GR|
         |GR|GR|GR|
         |RD|RD|RD|
         |YL|YL|YL|
         |YL|YL|YL|
|YL|ON|ON|BL|BL|BL|RD|RD|WT|
|YL|ON|ON|BL|BL|BL|RD|RD|WT|
|YL|ON|ON|BL|BL|BL|RD|RD|WT|
         |WT|WT|WT|
         |WT|WT|WT|
         |ON|ON|ON|"""
        self.cube.back_rotate()
        self.assertEqual(repr(self.cube),cube_repr)

    def test_complex_rotate(self):
        cube_repr = """         |GR|GR|YL|
         |GR|GR|YL|
         |ON|ON|YL|
         |YL|YL|RD|
         |YL|YL|BL|
         |YL|YL|BL|
|BL|BL|BL|RD|RD|WT|RD|RD|GR|
|ON|ON|ON|BL|BL|WT|RD|RD|GR|
|ON|ON|ON|BL|BL|WT|RD|RD|GR|
         |WT|WT|GR|
         |WT|WT|GR|
         |WT|WT|ON|"""
        self.cube.up_rotate()
        self.cube.right_rotate()
        self.assertEqual(repr(self.cube), cube_repr)

        cube_repr = """         |GR|GR|YL|
         |GR|GR|YL|
         |BL|BL|BL|
         |YL|YL|YL|
         |YL|YL|YL|
         |BL|BL|RD|
|RD|RD|WT|RD|RD|GR|YL|ON|ON|
|ON|ON|ON|BL|BL|WT|RD|RD|GR|
|ON|ON|ON|BL|BL|WT|RD|RD|GR|
         |WT|WT|GR|
         |WT|WT|GR|
         |WT|WT|ON|"""
        self.cube.up_rotate()
        self.assertEqual(repr(self.cube), cube_repr)

        cube_repr = """         |GR|GR|YL|
         |GR|GR|YL|
         |BL|BL|BL|
         |YL|YL|YL|
         |YL|YL|YL|
         |ON|ON|WT|
|RD|RD|WT|BL|BL|RD|BL|ON|ON|
|ON|ON|WT|BL|BL|RD|BL|RD|GR|
|ON|ON|GR|WT|WT|GR|RD|RD|GR|
         |RD|RD|YL|
         |WT|WT|GR|
         |WT|WT|ON|"""
        self.cube.front_rotate()
        self.assertEqual(repr(self.cube), cube_repr)

        cube_repr = """         |GR|GR|YL|
         |GR|GR|YL|
         |ON|ON|BL|
         |YL|YL|WT|
         |YL|YL|ON|
         |YL|YL|ON|
|BL|BL|BL|RD|RD|WT|BL|BL|RD|
|ON|ON|WT|BL|BL|RD|BL|RD|GR|
|ON|ON|GR|WT|WT|GR|RD|RD|GR|
         |RD|RD|YL|
         |WT|WT|GR|
         |WT|WT|ON|"""
        self.cube.up_rotate(clockwise=False)
        self.assertEqual(repr(self.cube), cube_repr)

        cube_repr = """         |YL|GR|YL|
         |YL|GR|YL|
         |YL|ON|BL|
         |RD|YL|WT|
         |BL|YL|ON|
         |WT|YL|ON|
|BL|WT|GR|RD|RD|WT|BL|BL|RD|
|BL|ON|ON|WT|BL|RD|BL|RD|GR|
|BL|ON|ON|WT|WT|GR|RD|RD|GR|
         |GR|RD|YL|
         |GR|WT|GR|
         |ON|WT|ON|"""
        self.cube.left_rotate(clockwise=False)
        self.assertEqual(repr(self.cube), cube_repr)

        cube_repr = """         |GR|RD|RD|
         |YL|GR|YL|
         |YL|ON|BL|
         |RD|YL|WT|
         |BL|YL|ON|
         |WT|YL|ON|
|BL|WT|GR|RD|RD|WT|BL|BL|RD|
|BL|ON|ON|WT|BL|RD|BL|RD|GR|
|YL|GR|YL|BL|ON|ON|WT|WT|GR|
         |ON|GR|GR|
         |WT|WT|RD|
         |ON|GR|YL|"""
        self.cube.down_rotate()
        self.assertEqual(repr(self.cube), cube_repr)

    def test_is_solved(self):
        self.assertEqual(self.cube.is_solved(), True)
        self.cube.down_rotate()
        self.assertEqual(self.cube.is_solved(), False)
        self.cube.down_rotate(clockwise=False)
        self.assertEqual(self.cube.is_solved(), True)

    def test_comparison(self):
        second_cube = Cube()
        self.assertEqual(self.cube, second_cube)
        second_cube.up_rotate()
        self.assertNotEqual(self.cube, second_cube)
        second_cube.up_rotate()
        second_cube.up_rotate()
        second_cube.up_rotate()
        self.assertEqual(self.cube, second_cube)
