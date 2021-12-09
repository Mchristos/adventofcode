from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np


def process_inputs(inputs: list[str]):
    return np.array([[int(y) for y in list(x)] for x in inputs])


def get_lowpoints(heights):
    rows, cols = heights.shape
    lowpoints = []
    for i in range(rows):
        for j in range(cols):
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
                lowpoints.append([i, j])
    return lowpoints
    return np.sum(lowpoints) + len(lowpoints)


def expand(point, heights):
    i, j = point
    rows, cols = heights.shape
    expanded_points = []
    # expand in the vertical direction
    if i > 0 and heights[i - 1, j] > heights[i, j] and heights[i - 1, j] != 9:
        expanded_points.append([i - 1, j])
    if (i < rows - 1) and heights[i, j] < heights[i + 1, j] and heights[i + 1, j] != 9:
        expanded_points.append([i + 1, j])
    # expand in the horizontal direction
    if j > 0 and heights[i, j - 1] > heights[i, j] and heights[i, j - 1] != 9:
        expanded_points.append([i, j - 1])
    if (j < cols - 1) and heights[i, j] < heights[i, j + 1] and heights[i, j + 1] != 9:
        expanded_points.append([i, j + 1])
    return expanded_points


def get_basins(heights):
    lowpoints = get_lowpoints(heights)
    basins = []
    for lowpoint in lowpoints:
        # expand point to build up the basin
        basin = [lowpoint]
        while True:
            new_basin = basin
            # expand each point in the basin
            for point in basin:
                print("Expanding: ", point)
                expanded = expand(point, heights)
                for expanded_point in expanded:
                    if expanded_point not in basin:
                        new_basin.append(expanded_point)
            print(new_basin)
            if len(new_basin) == len(basin):
                break
            else:
                basin = new_basin
        basins.append(basin)
    return basins


inputs = read_input("./inputs/day9.txt")
heightmap = process_inputs(inputs)
print(heightmap)

begin_part_one()
solution()
begin_part_two()
basins = get_basins(heightmap)
basin_sizes = sorted([len(basin) for basin in basins], reverse=True)
print(basin_sizes)

solution(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
