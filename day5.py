from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np

n_grid = 1000


def string_to_array(value):
    return np.array([int(x) for x in value.split(",")])


def process_input(inputs: list[str]):
    # return [ np.array(string_to_array(start), string_to_array(end)) for value in inputs for (start, end) in value.split(' -> ') ]
    result = []
    for value in inputs:
        start, end = value.split(" -> ")
        result.append(np.array([string_to_array(start), string_to_array(end)]))
    return result


lines = process_input(read_input("./inputs/day5.txt"))
begin_part_one()
grid = np.zeros([n_grid, n_grid])
for line in lines:
    # vertical
    if line[0, 0] == line[1, 0]:
        x = line[0, 0]
        miny = min(line[0, 1], line[1, 1])
        maxy = max(line[0, 1], line[1, 1])
        # print(f"line at x={x} from y={miny} to y={maxy}")
        for y in range(miny, maxy + 1):
            grid[x, y] += 1
    # horizontal
    elif line[0, 1] == line[1, 1]:
        y = line[0, 1]
        minx = min(line[0, 0], line[1, 0])
        maxx = max(line[0, 0], line[1, 0])
        # print(f"line at y={y} from y={minx} to y={maxx}")
        for x in range(minx, maxx + 1):
            grid[x, y] += 1
    # diagonal
    else:
        print(
            f"found diagonal from x={line[0,0]}->{line[1,0]} and y={line[0,1]}->{line[1,1]}"
        )
        x_direction = 1 if line[0, 0] < line[1, 0] else -1
        y_direction = 1 if line[0, 1] < line[1, 1] else -1
        for (i, x) in enumerate(
            range(line[0, 0], line[1, 0] + x_direction, x_direction)
        ):
            y = line[0, 1] + i * y_direction
            grid[x, y] += 1

solution()
begin_part_two()
print(grid.transpose())
solution(np.sum(grid >= 2))
