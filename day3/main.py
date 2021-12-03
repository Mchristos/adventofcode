import numpy as np

def read_input(path: str) -> list[str]: 
    with open(path, 'r') as file: 
        return file.read().split('\n')

def process_input(lines: list[str]):
    return  np.array([[int(digit) for digit in line] for line in lines])

def binaryarraytoint(array):
    return int(str("".join([str(x) for x in array])), 2)

def compute_gamma(readings: np.array):
    return (np.sum(readings, axis=0) >= (readings.shape[0]/2)).astype(int)

def compute_epsilon(readings: np.array):
    return (np.sum(readings, axis=0) < (readings.shape[0]/2)).astype(int)


values = process_input(read_input("../inputs/day3.txt"))

print("--- Part One ---\n")
print(np.sum(values, axis=0))
gamma = compute_gamma(values)
epsilon = compute_epsilon(values)
print("gamma:   ", gamma)
print("epsilon: ", epsilon)
print(binaryarraytoint(gamma))
print(binaryarraytoint(epsilon))
print(binaryarraytoint(gamma)*binaryarraytoint(epsilon))

print("--- Part Two ---\n")

def get_oxygen_rating(numbers):
    i = 0
    while len(numbers) > 1:
        filter = [(row[i] == compute_gamma(numbers)[i]) for row in numbers]
        numbers = numbers[filter, :]
        # if len(numbers) < 8:
        #     print(i)
        #     print(numbers)
        i += 1
    return numbers[0]

def get_scrubber_rating(numbers):
    i = 0
    while len(numbers) > 1:
        filter = [(row[i] == compute_epsilon(numbers)[i]) for row in numbers]
        numbers = numbers[filter, :]
        if len(numbers) < 8:
            print(i)
            print(numbers)
        i += 1
    return numbers[0]

oxygen_rating = get_oxygen_rating(values)
scrubber_rating = get_scrubber_rating(values)
print(oxygen_rating)
print(scrubber_rating)
print(binaryarraytoint(oxygen_rating))
print(binaryarraytoint(scrubber_rating))
print(binaryarraytoint(oxygen_rating)*binaryarraytoint(scrubber_rating))
print("------------------- \n")
