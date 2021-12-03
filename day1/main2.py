n_window = 3


def count_increases(numbers):
    count = 0
    for (i, number) in enumerate(numbers):
        if i == 0:
            continue
        if number > numbers[i - 1]:
            count += 1
    return count


with open("../inputs/day1.txt", "r") as file:
    text = file.read()
    numbers = list(map(lambda x: int(x), text.split("\n")))
    window_values = []
    for i in range(len(numbers) - n_window + 1):
        window = numbers[i : i + n_window]
        print(window)
        value = sum(numbers[i : i + n_window])
        print(value)
        window_values.append(value)
    print("-----------------")
    print(len(numbers), len(window_values))
    print(count_increases(window_values))
