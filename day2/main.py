def read_input():
    with open('../inputs/day2.txt', 'r') as file: 
        text = file.read()
        return text

def process_input(text: str):
    steps = [line.split(' ') for line in text.split('\n')]
    return [(step[0], int(step[1])) for step in steps ]

def calculate_position(steps: list[tuple[str,int]]):
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

def calculate_position_part2(steps: list[tuple[str,int]]):
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

steps = process_input(read_input())

# Part One
position = calculate_position(steps)
print(position)
print(position[0] * position[1])

# Part Two 
position = calculate_position_part2(steps)
print(position)
print(position[0] * position[1])
