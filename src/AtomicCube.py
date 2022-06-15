

class AtomicCube(object):
    def __init__(self):
        self.upper_face = "YL"
        self.down_face = "WT"
        self.front_face = "BL"
        self.back_face = "GR"
        self.right_face = "RD"
        self.left_face = "ON"

    def __eq__(self, obj):
        if self.upper_face != obj.upper_face:
            return False
        if self.down_face != obj.down_face:
            return False
        if self.front_face != obj.front_face:
            return False
        if self.back_face != obj.back_face:
            return False
        if self.right_face != obj.right_face:
            return False
        if self.left_face != obj.left_face:
            return False
        return True

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        ret = ""
        ret += "   |%s|\n" % (self.back_face)
        ret += "   |%s|\n" % (self.upper_face)
        ret += "|%s|%s|%s|\n" % (self.left_face, self.front_face, self.right_face)
        ret += "   |%s|" % (self.down_face)
        return ret

    def show_face(self, face):
        faces = {
            "U":self.upper_face,
            "D":self.down_face,
            "F":self.front_face,
            "B":self.back_face,
            "R":self.right_face,
            "L":self.left_face}
        return faces[face]

    def up_rotate(self, clockwise=True):
        if clockwise:
            tmp = self.front_face
            self.front_face = self.right_face
            self.right_face = self.back_face
            self.back_face = self.left_face
            self.left_face = tmp
        else:
            tmp = self.front_face
            self.front_face = self.left_face
            self.left_face = self.back_face
            self.back_face = self.right_face
            self.right_face = tmp

    def down_rotate(self, clockwise=True):
        self.up_rotate(True^clockwise)


    def front_rotate(self, clockwise=True):
        if clockwise:
            tmp = self.upper_face
            self.upper_face = self.left_face
            self.left_face = self.down_face
            self.down_face = self.right_face
            self.right_face = tmp
        else:
            tmp = self.upper_face
            self.upper_face = self.right_face
            self.right_face = self.down_face
            self.down_face = self.left_face
            self.left_face = tmp

    def back_rotate(self, clockwise=True):
        self.front_rotate(True^clockwise)

    def right_rotate(self, clockwise=True):
        if clockwise:
            tmp = self.upper_face
            self.upper_face = self.front_face
            self.front_face = self.down_face
            self.down_face = self.back_face
            self.back_face = tmp
        else:
            tmp = self.upper_face
            self.upper_face = self.back_face
            self.back_face = self.down_face
            self.down_face = self.front_face
            self.front_face = tmp

    def left_rotate(self, clockwise=True):
        self.right_rotate(True^clockwise)


def test():
    ac = AtomicCube()
    print(ac)
    print ("--")
    ac.up_rotate()
    print(ac)
    print ("--")
    ac.up_rotate()
    print(ac)
    print ("--")
    ac.up_rotate(clockwise=False)
    print(ac)

    print ("--")
    ac.down_rotate()
    print (ac)
    print ("--")
    ac.down_rotate(clockwise=False)
    print (ac)


if __name__ == "__main__":
    test()