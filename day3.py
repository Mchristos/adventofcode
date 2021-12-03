import numpy as np
from helpers import read_input, begin_part_one, begin_part_two, solution


def process_input(lines: list[str]):
    return np.array([[int(digit) for digit in line] for line in lines])


begin_part_one()
values = process_input(read_input("./inputs/day3.txt"))


def binaryarraytoint(array):
    return int(str("".join([str(x) for x in array])), 2)


def compute_gamma(readings: np.array):
    return (np.sum(readings, axis=0) >= (readings.shape[0] / 2)).astype(int)


def compute_epsilon(readings: np.array):
    return (np.sum(readings, axis=0) < (readings.shape[0] / 2)).astype(int)


gamma = compute_gamma(values)
epsilon = compute_epsilon(values)
print("gamma:   ", gamma, binaryarraytoint(gamma))
print("epsilon: ", epsilon, binaryarraytoint(epsilon))
solution(binaryarraytoint(gamma) * binaryarraytoint(epsilon))

begin_part_two()


def get_oxygen_rating(numbers):
    i = 0
    while len(numbers) > 1:
        filter = [(row[i] == compute_gamma(numbers)[i]) for row in numbers]
        numbers = numbers[filter, :]
        i += 1
    return numbers[0]


def get_scrubber_rating(numbers):
    i = 0
    while len(numbers) > 1:
        filter = [(row[i] == compute_epsilon(numbers)[i]) for row in numbers]
        numbers = numbers[filter, :]
        i += 1
    return numbers[0]


oxygen_rating = get_oxygen_rating(values)
scrubber_rating = get_scrubber_rating(values)
print("oxygen rating: ", oxygen_rating, binaryarraytoint(oxygen_rating))
print("scrubber rating: ", scrubber_rating, binaryarraytoint(scrubber_rating))
solution(binaryarraytoint(oxygen_rating) * binaryarraytoint(scrubber_rating))
