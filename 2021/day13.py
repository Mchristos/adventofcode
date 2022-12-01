from numpy.core.fromnumeric import shape
from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np

input = read_input("./inputs/day13.txt")
instructions = read_input("./inputs/day13_folds.txt")


def fold(dots, index, axis="x"):
    if axis == "y":
        # fold along y
        top = dots[:, :index]
        bottom = dots[:, index + 1 :]
        pad_size = top.shape[1] - bottom.shape[1]
        if pad_size >= 0:
            bottom = np.pad(bottom.T, [[0, pad_size], [0, 0]]).T
        else:
            raise Exception(f"Bottom half of fold is too long")
        flipped = np.flip(bottom, axis=1)
        return np.ones(top.shape) * ((top + flipped) > 0)
    if axis == "x":
        # fold along x
        left = dots[:index, :]
        right = dots[index + 1 :, :]
        if right.shape[0] < left.shape[0]:
            right = np.pad(right.T, [[0, 0], [0, 1]]).T
        flipped = np.flip(right, axis=0)
        return np.ones(left.shape) * ((left + flipped) > 0)


positions = []
for line in input:
    if line == "":
        break
    positions.append([int(x) for x in line.split(",")])

dots = np.zeros(
    [max([pos[0] for pos in positions]) + 1, max([pos[1] for pos in positions]) + 1]
)
for position in positions:
    dots[position[0], position[1]] = 1


begin_part_one()
folded = fold(dots, 655, "x")
solution(np.sum(folded))


begin_part_two()
state = dots
for instruction in instructions:
    axis, index = instruction.split(" ")[-1].split("=")
    index = int(index)
    state = fold(state, index, axis)
solution()
for i in range(8):
    print(state[i * 5 : (i + 1) * 5, :].T)
    print()
