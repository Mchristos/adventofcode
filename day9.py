from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np


def process_inputs(inputs: list[str]):
    return np.array([[int(y) for y in list(x)] for x in inputs])


def solve(heights):
    rows, cols = heights.shape
    lowpoints = []
    for i in range(rows):
        for j in range(cols):
            # is it a verticallly low point
            is_vert_low = False
            if i == 0 or heights[i - 1, j] > heights[i, j]:
                if (i == rows - 1) or heights[i, j] < heights[i + 1, j]:
                    is_vert_low = True
            is_horiz_low = False
            if j == 0 or heights[i, j - 1] > heights[i, j]:
                if (j == cols - 1) or heights[i, j] < heights[i, j + 1]:
                    is_horiz_low = True
            if is_horiz_low and is_vert_low:
                # print(f"{i, j} is low")
                lowpoints.append(heights[i, j])
    print(lowpoints)
    return np.sum(lowpoints) + len(lowpoints)


inputs = read_input("./inputs/day9.txt")
heightmap = process_inputs(inputs)
print(heightmap)

begin_part_one()
solution(solve(heightmap))
begin_part_two()
solution()
