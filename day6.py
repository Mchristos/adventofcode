from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np

n_days = 80


def next_state(fish: np.ndarray):
    n_births = np.sum(fish == 0)
    next = (fish - 1) % 7
    # Correct the 8 -> 7 transition that is incorrect
    for i in np.where(fish == 8)[0]:
        next[i] = 7
    return np.append(next, 8 * np.ones(n_births, dtype=int))


fish = np.array(
    [
        int(value)
        for value in read_input("./inputs/day6.txt", splitlines=False).split(",")
    ]
)

begin_part_one()
for i in range(n_days):
    fish = next_state(fish)
print(f"Final state: {fish}")
solution(len(fish))
begin_part_two()
solution()
