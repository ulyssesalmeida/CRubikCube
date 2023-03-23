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
        colors = {"RD": "\u001b[31m",
                 "GR": "\u001b[32m",
                 "YL": "\u001b[33m",
                 "BL": "\u001b[34m",
                 "ON": "\u001b[35m",
                 "WT": "\u001b[37m",
                 "Reset": "\u001b[0m" }

        str_repr = repr(self.cube)
        for color in colors:
            str_repr = str_repr.replace(color,f"{colors[color]}{color}{colors['Reset']}")
        return str_repr

    def read_command(self):
        return input(self.terminal())
    
if __name__ == "__main__":
    cli = CLI()
    print(cli.welcome_message())
    print(cli.print_cube())
    while True:
        typed_cmds = cli.read_command()
        for cmd in typed_cmds.split(","):
            if cmd == "help":
                print(cli.help_message())
            if cmd in ["exit", "quit"]:
                break
            if cmd == "U":
                cli.cube.up_rotate()
            if cmd == "U'":
                cli.cube.up_rotate(clockwise=False)
            if cmd == "D":
                cli.cube.down_rotate()
            if cmd == "D'":
                cli.cube.down_rotate(clockwise=False)
            if cmd == "F":
                cli.cube.front_rotate()
            if cmd == "F'":
                cli.cube.front_rotate(clockwise=False)
            if cmd == "B":
                cli.cube.back_rotate()
            if cmd == "B'":
                cli.cube.back_rotate(clockwise=False)
            if cmd == "R":
                cli.cube.right_rotate()
            if cmd == "R'":
                cli.cube.right_rotate(clockwise=False)
            if cmd == "L":
                cli.cube.left_rotate()
            if cmd == "L'":
                cli.cube.left_rotate(clockwise=False)
            print(cli.print_cube())
            if cli.cube.is_solved():
                print("--- SOLVED")
            else:
                print("---")
        if cmd in ["exit", "quit"]:
            break
