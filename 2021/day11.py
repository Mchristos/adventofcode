from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np


def find_adj(i, length):
    i_vals = []
    if i > 0:
        i_vals.append(i - 1)
    if i < length - 1:
        i_vals.append(i + 1)
    return i_vals


def find_adjacent(i, j, shape):
    i_vals = find_adj(i, shape[0])
    j_vals = find_adj(j, shape[1])
    return (
        [(i, j_) for j_ in j_vals]
        + [(i_, j) for i_ in i_vals]
        + [(i_, j_) for i_ in i_vals for j_ in j_vals]
    )


def flash(energies: np.ndarray, flash_count=0):
    new_energies = np.array(energies)
    for i in range(energies.shape[0]):
        for j in range(energies.shape[1]):
            # flash only at 10 insures a single flash
            if energies[i, j] == 10:
                flash_count += 1
                new_energies[i, j] += 1
                adjacent_vals = find_adjacent(i, j, energies.shape)
                for (i_, j_) in adjacent_vals:
                    if new_energies[i_, j_] < 10:
                        new_energies[i_, j_] += 1
    if (new_energies == 10).any():
        return flash(new_energies, flash_count)
    else:
        return new_energies, flash_count


lines = read_input("./inputs/day11.txt")
energies = np.array([[int(x) for x in line] for line in lines], dtype=int)
print(energies)

begin_part_one()
flashes = 0
for step in range(1000):
    # increment
    energies = energies + 1
    # flash
    energies, flash_count = flash(energies)
    flashes += flash_count
    # set to 0
    energies[energies > 9] = 0
    if np.all(energies == 0):
        print(energies)
        print(step + 1)
        break
# print(energies)
solution(flashes)


begin_part_two()
solution()
