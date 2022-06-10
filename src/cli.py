import sys

from Cube import Cube

class CLI(object):
    def __init__(self):
        self.cube = Cube()
        self.version = "1.0 [branch: ahead, commit: 4632e2b]"
    
    def welcome_message(self):
        return """CRubikCube %s on Python %s
Type "help" for more information""" % (self.version, sys.version)
    
    def help_message(self):
        return """No help yet. Sorry!"""
    
    def terminal(self):
        return ">>> "
    
    def print_cube(self):
        return repr(self.cube)

    def read_command(self):
        return input(self.terminal())
    
if __name__ == "__main__":
    cli = CLI()
    print(cli.welcome_message())
    print(cli.print_cube())
    cmd = cli.read_command()
    while not cmd in ["exit","quit"]:
        if cmd == "help":
            print(cli.help_message())
        if cmd == "U":
            cli.cube.up_rotate()
        print(cli.print_cube())
        cmd = cli.read_command()