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

