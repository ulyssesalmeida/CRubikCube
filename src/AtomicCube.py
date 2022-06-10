

class AtomicCube(object):
    def __init__(self):
        self.upper_face = "YL"
        self.down_face = "WT"
        self.front_face = "BL"
        self.back_face = "GR"
        self.right_face = "RD"
        self.left_face = "ON"

    def __str__(self):
        ret = ""
        ret += "   |%s|\n" % (self.back_face)
        ret += "   |%s|\n" % (self.upper_face)
        ret += "|%s|%s|%s|\n" % (self.left_face, self.front_face, self.right_face)
        ret += "   |%s|" % (self.down_face)
        return ret

    def up_rotate(self):
        tmp = self.front_face
        self.front_face = self.right_face
        self.right_face = self.back_face
        self.back_face = self.left_face
        self.left_face = tmp


def test():
    ac = AtomicCube()
    print(ac)

if __name__ == "__main__":
    test()