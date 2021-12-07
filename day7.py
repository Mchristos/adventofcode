from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np


def compute_fuel(positions, point):
    fuel = [np.sum(range(1, x + 1)) for x in np.abs(positions - point)]
    return np.sum(fuel)


def solve(positions: np.ndarray, radius=10):
    mean = int(np.round(np.mean(positions)))
    print("mean =", mean)
    min_fuel = compute_fuel(positions, mean)
    print(min_fuel)
    for i in range(radius):
        if i < mean:
            fuel_left = compute_fuel(positions, mean - i)
            if fuel_left < min_fuel:
                min_fuel = fuel_left
        fuel_right = compute_fuel(positions, mean + i)
        if fuel_right < min_fuel:
            min_fuel = fuel_right
        print(min_fuel)
    return min_fuel


input = read_input("./inputs/day7.txt", splitlines=False)
crabmarines = np.array([int(x) for x in input.split(",")], dtype=int)
# crabmarines = np.array([16,1,2,0,4,2,7,1,2,14], dtype=int)

begin_part_one()
begin_part_two()
solution(solve(crabmarines))
solution()
