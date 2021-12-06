from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np


def next_fish(fish: np.ndarray):
    n_births = np.sum(fish == 0)
    next = (fish - 1) % 7
    # Correct the 8 -> 7 transition that is incorrect
    for i in np.where(fish == 8)[0]:
        next[i] = 7
    return np.append(next, 8 * np.ones(n_births, dtype=int))


def next_state(state: np.ndarray):
    next = np.roll(state, -1)
    # 0 day fish go to day 6, joining those that came from day 7
    next[6] = next[6] + state[0]
    return next


fish = np.array(
    [
        int(value)
        for value in read_input("./inputs/day6.txt", splitlines=False).split(",")
    ]
)

begin_part_one()
n_days = 80
fish_state = fish
for i in range(n_days):
    fish_state = next_fish(fish)
print(f"Final state: {fish_state}")
solution(len(fish_state))
begin_part_two()
n_days = 256
# The state defines the number of fish in state i at index i
state = np.array([np.sum(fish == i) for i in range(9)], dtype=float)
for i in range(n_days):
    state = next_state(state)
solution(int(np.sum(state)))
