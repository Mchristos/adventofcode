from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np


def compute_fuel(positions, point, ramping):
    fuel = np.abs(positions - point)
    if ramping:
        fuel = [np.sum(range(1, x + 1)) for x in fuel]
    return np.sum(fuel)


def solve(positions: np.ndarray, radius=10, ramping=False):
    mean = int(np.round(np.mean(positions)))
    min_fuel = compute_fuel(positions, mean, ramping)
    for i in range(radius):
        if i < mean:
            fuel_left = compute_fuel(positions, mean - i, ramping)
            if fuel_left < min_fuel:
                min_fuel = fuel_left
        fuel_right = compute_fuel(positions, mean + i, ramping)
        if fuel_right < min_fuel:
            min_fuel = fuel_right
    return min_fuel


input = read_input("./inputs/day7.txt", splitlines=False)
crabmarines = np.array([int(x) for x in input.split(",")], dtype=int)

begin_part_one()
solution(solve(crabmarines, radius=500))
begin_part_two()
solution(solve(crabmarines, ramping=True))
