import copy

from AtomicCube import AtomicCube

class Cube(object):
    def __init__(self):
        self.cube = []
        for i in range(3):
            layer = []
            for j in range(3):
                line = [AtomicCube(), AtomicCube(), AtomicCube()]
                layer.append(line)
            self.cube.append(layer)

    def __repr__(self):
        b_layer = self.get_back_layer()
        u_layer = self.get_up_layer()
        l_layer = self.get_left_layer()
        f_layer = self.get_front_layer()
        r_layer = self.get_right_layer()
        d_layer = self.get_down_layer()

        ret = ""
        for i in range(3):
            ret += "         |" + self.print_face_line("B", b_layer[i], "|")
            ret += "|\n"
        for i in range(3):
            ret += "         |" + self.print_face_line("U", u_layer[i], "|")
            ret += "|\n"
        for i in range(3):
            ret += "|" + self.print_face_line("L", l_layer[i], "|") + "|" + self.print_face_line("F", f_layer[i], "|") + "|" + self.print_face_line("R", r_layer[i], "|")
            ret += "|\n"
        for i in range(3):
            ret += "         |" + self.print_face_line("D", d_layer[i], "|")
            ret += "|\n"
        return ret[:-1]

    def get_layer(self, face):
        layer = {
        "U":self.get_up_layer,
        "D":self.get_down_layer,
        "F":self.get_front_layer,
        "B":self.get_back_layer,
        "R":self.get_right_layer,
        "L":self.get_left_layer,
        }
        return layer[face]()

    def get_up_layer(self):
        layer = []
        for i in range(2,-1,-1):
            line = []
            for j in range(3):
                line.append(self.cube[j][0][i])
            layer.append(line)
        return layer

    def get_down_layer(self):
        layer = []
        for i in range(3):
            line = []
            for j in range(3):
                line.append(self.cube[j][2][i])
            layer.append(line)
        return layer

    def get_front_layer(self):
        layer = []
        for i in range(3):
            line = []
            for j in range(3):
                line.append(self.cube[j][i][0])
            layer.append(line)
        return layer

    def get_back_layer(self):
        layer = []
        for i in range(2,-1,-1):
            line = []
            for j in range(3):
                line.append(self.cube[j][i][2])
            layer.append(line)
        return layer

    def get_right_layer(self):
        layer = []
        for i in range(3):
            line = []
            for j in range(3):
                line.append(self.cube[2][i][j])
            layer.append(line)
        return layer

    def get_left_layer(self):
        layer = []
        for i in range(3):
            line = []
            for j in range(2,-1,-1):
                line.append(self.cube[0][i][j])
            layer.append(line)
        return layer

    def print_face_line(self, face, line, separator):
        return separator.join([atomic_cube.show_face(face) for atomic_cube in line])

    def print_face(self, face):
        ret = ""
        for line in self.get_layer(face):
            ret += "|"
            ret += self.print_face_line(face, line, "|")
            ret += "|\n"
        return ret[:-1]

    def down_rotate(self, clockwise = True, layer = 2):
        self.up_rotate(clockwise = clockwise^True, layer = 2)

    def up_rotate(self, clockwise = True, layer = 0):
        cube_copy = copy.deepcopy(self.cube)
        if clockwise:
            for i in range(3):
                for j in range(3):
                    self.cube[i][layer][j] = cube_copy[2-j][layer][i]
                    self.cube[i][layer][j].up_rotate(clockwise)
        else:
            for i in range(3):
                for j in range(3):
                    self.cube[2-j][layer][i] = cube_copy[i][layer][j]
                    self.cube[2-j][layer][i].up_rotate(clockwise)

    def left_rotate(self, clockwise = True, layer = 0):
        self.right_rotate(clockwise = clockwise^True, layer = 0)

    def right_rotate(self, clockwise = True, layer = 2):
        cube_copy = copy.deepcopy(self.cube)
        if clockwise:
            for i in range(3):
                for j in range(3):
                    self.cube[layer][i][j] = cube_copy[layer][2-j][i]
                    self.cube[layer][i][j].right_rotate(clockwise)
        else:
            for i in range(3):
                for j in range(3):
                    self.cube[layer][2-j][i] = cube_copy[layer][i][j]
                    self.cube[layer][2-j][i].right_rotate(clockwise)

    def front_rotate(self, clockwise = True, layer = 0):
        self.back_rotate(clockwise = clockwise^True, layer = 0)

    def back_rotate(self, clockwise = True, layer = 2):
        cube_copy = copy.deepcopy(self.cube)
        if clockwise:
            for i in range(3):
                for j in range(3):
                    self.cube[i][j][layer] = cube_copy[2-j][i][layer]
                    self.cube[i][j][layer].back_rotate(clockwise)
        else:
            for i in range(3):
                for j in range(3):
                    self.cube[2-j][i][layer] = cube_copy[i][j][layer]
                    self.cube[2-j][i][layer].back_rotate(clockwise)

if __name__ == "__main__":
    c = Cube()
    c.up_rotate()
    c.right_rotate()
    c.up_rotate()
    c.front_rotate()
    print(repr(c))
