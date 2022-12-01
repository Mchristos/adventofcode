from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np

n_grid = 1000


def string_to_array(value):
    return np.array([int(x) for x in value.split(",")])


def process_input(inputs: list[str]):
    result = []
    for value in inputs:
        start, end = value.split(" -> ")
        result.append(np.array([string_to_array(start), string_to_array(end)]))
    return result


def solve(lines: list[np.ndarray], diagonals=False):
    grid = np.zeros([n_grid, n_grid])
    for line in lines:
        (x1, y1), (x2, y2) = line
        # vertical
        if x1 == x2:
            grid[x1, min(y1, y2) : max(y1, y2) + 1] += 1
        # horizontal
        elif y1 == y2:
            grid[min(x1, x2) : max(x1, x2) + 1, y1] += 1
        # diagonal
        else:
            if not diagonals:
                continue
            dx = 1 if x1 < x2 else -1
            dy = 1 if y1 < y2 else -1
            for (i, x) in enumerate(range(x1, x2 + dx, dx)):
                y = line[0, 1] + i * dy
                grid[x, y] += 1
    return np.sum(grid >= 2)


lines = process_input(read_input("./inputs/day5.txt"))
begin_part_one()
solution(solve(lines))
begin_part_two()
solution(solve(lines, diagonals=True))
