import sys

import copy
import random
import itertools

from Cube import Cube

class CubeSolver(object):
    def __init__(self, cube: Cube) -> None:
        self.cube = cube
        self.moves = []
        self.states = []
        self.try_movements_count = 0

    def solve_itertools(self) -> None:
        moves = ["U", "D", "F", "B", "R", "L", "U'", "D'", "F'", "B'", "R'", "L'"]
        nmoves = 1
        while nmoves < 50:
            print (f"nmoves = {nmoves}")
            # possible_sequences = [p for p in itertools.product(moves, repeat=nmoves)]
            for sequence in itertools.product(moves, repeat=nmoves):
                check = self.try_sequence(sequence)
                if check:
                    print (f"Total de {self.try_movements_count} tentativas")
                    print (sequence)
                    self.moves = sequence
                    return sequence
            nmoves+=1

    def try_sequence(self, sequence: list) -> bool:
        # print (f"Trying {sequence}")
        cube = copy.deepcopy(self.cube)
        states = []
        last_move = ""
        same_move_seq = 0
        move_count = 0
        for move in sequence:
            move_count+=1
            self.try_movements_count+=1
            clockwise = True
            if move == last_move:
                same_move_seq += 1
                if same_move_seq >= 2:
                    print (f"Skipping 1 [{len(sequence)}] -> {sequence} on {move_count} -> {move}")
                    return False
            else:
                same_move_seq = 0
                if move.replace("'","") == last_move:
                    print (f"Skipping 3 [{len(sequence)}] -> {sequence} on {move_count} -> {move}:{last_move}")
                    return False
                if last_move.replace("'","") == move:
                    print (f"Skipping 3 [{len(sequence)}] -> {sequence} on {move_count} -> {move}:{last_move}")
                    return False
            last_move = move
            if "'" in move:
                clockwise=False
            if "U" in move:
                cube.up_rotate(clockwise)
            elif "D" in move:
                cube.down_rotate(clockwise)
            elif "F" in move:
                cube.front_rotate(clockwise)
            elif "B" in move:
                cube.back_rotate(clockwise)
            elif "R" in move:
                cube.right_rotate(clockwise)
            elif "L" in move:
                cube.left_rotate(clockwise)
            if cube in states:
                print (f"Skipping 2 [{len(sequence)}] -> {sequence} on {move_count} -> {move}")
                return False
            else:
                states.append(copy.deepcopy(cube))
        return cube.is_solved()

    def solve_random(self) -> None:
        self.states.append(copy.deepcopy(self.cube))
        while not self.cube.is_solved():
            next_move = random.choice(["U", "D", "F", "B", "R", "L"])
            print(f"{len(self.moves)}: U:{'U' in self.moves} D:{'D' in self.moves} F:{'F' in self.moves} B:{'B' in self.moves} R:{'R' in self.moves} L:{'L' in self.moves} / SIZE: {sys.getsizeof(self.states)} / NEXT: {next_move}")
            if self.try_move(next_move):
                self.cube.up_rotate()
                self.moves.append(next_move)
                self.states.append(copy.deepcopy(self.cube))

    def solve(self):
        self.states.append(copy.deepcopy(self.cube))
        while not self.cube.is_solved():
            print(f"{len(self.moves)}: U:{'U' in self.moves} D:{'D' in self.moves} F:{'F' in self.moves} B:{'B' in self.moves} R:{'R' in self.moves} L:{'L' in self.moves} / SIZE: {sys.getsizeof(self.states)}")
            if self.try_move("U"):
                self.cube.up_rotate()
                self.moves.append("U")
                self.states.append(copy.deepcopy(self.cube))
                continue
            if self.try_move("D"):
                self.cube.down_rotate()
                self.moves.append("D")
                self.states.append(copy.deepcopy(self.cube))
                continue
            if self.try_move("F"):
                self.cube.front_rotate()
                self.moves.append("F")
                self.states.append(copy.deepcopy(self.cube))
                continue
            if self.try_move("B"):
                self.cube.back_rotate()
                self.moves.append("B")
                self.states.append(copy.deepcopy(self.cube))
                continue
            if self.try_move("R"):
                self.cube.right_rotate()
                self.moves.append("R")
                self.states.append(copy.deepcopy(self.cube))
                continue
            if self.try_move("L"):
                self.cube.left_rotate()
                self.moves.append("L")
                self.states.append(copy.deepcopy(self.cube))
                continue

    def try_move(self, move: str) -> bool:
        cube = copy.deepcopy(self.cube)
        if move == "U":
            cube.up_rotate()
        elif move == "D":
            cube.down_rotate()
        elif move == "F":
            cube.front_rotate()
        elif move == "B":
            cube.back_rotate()
        elif move == "R":
            cube.right_rotate()
        elif move == "L":
            cube.left_rotate()
        if cube.is_solved():
            return True
        if not cube in self.states:
            return True
        return False

if __name__ == "__main__":
    c = Cube()
    c.front_rotate()
    c.up_rotate(clockwise=False)
    c.down_rotate(clockwise=False)
    c.up_rotate(clockwise=False)
    c.front_rotate(clockwise=False)
    c.right_rotate()
    cs = CubeSolver(c)
    # cs.solve()
    # cs.solve_random()
    cs.solve_itertools()

    print (f"{c in cs.states}")
    print (f"{len(cs.moves)}")
    print (f"Sequencia: {cs.moves}")