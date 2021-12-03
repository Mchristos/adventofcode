from helpers import read_input, begin_part_one, begin_part_two, solution


def process_input(input: str):
    steps = [line.split(" ") for line in input]
    return [(step[0], int(step[1])) for step in steps]


def calculate_position(steps: list[tuple[str, int]]):
    horizontal = 0
    depth = 0
    for step in steps:
        if step[0] == "forward":
            horizontal += step[1]
        elif step[0] == "down":
            depth += step[1]
        elif step[0] == "up":
            depth -= step[1]
        else:
            raise Exception(f"Invalid direction {step[0]}")
    return (horizontal, depth)


def calculate_position_part2(steps: list[tuple[str, int]]):
    horizontal = 0
    depth = 0
    aim = 0
    for step in steps:
        if step[0] == "forward":
            horizontal += step[1]
            depth += aim * step[1]
        elif step[0] == "down":
            aim += step[1]
        elif step[0] == "up":
            aim -= step[1]
        else:
            raise Exception(f"Invalid direction {step[0]}")
    return (horizontal, depth, aim)


steps = process_input(read_input("inputs/day2.txt"))

begin_part_one()
position = calculate_position(steps)
solution(position[0] * position[1])

begin_part_two()
position = calculate_position_part2(steps)
solution(position[0] * position[1])
