from helpers import read_input, begin_part_one, begin_part_two, solution


def count_chars(string: str, char: str):
    return len([char_ for char_ in string if char_ == char])


inputs = read_input("./inputs/day14.txt")
polymer = inputs[0]
rules = [rule.split(" -> ") for rule in inputs[2:]]


begin_part_one()
for i in range(10):
    newpolymer = ""
    for i in range(len(polymer) - 1):
        pair = polymer[i : i + 2]
        applicable = [rule for rule in rules if pair == rule[0]]
        if len(applicable) > 0:
            rule = applicable[0]
            newpolymer = newpolymer + pair[0] + rule[1]
        else:
            newpolymer = newpolymer + pair[0]
    newpolymer = newpolymer + polymer[-1]
    polymer = newpolymer

unique_chars = set(list(polymer))
char_counts = [count_chars(polymer, char) for char in unique_chars]
solution(max(char_counts) - min(char_counts))


begin_part_two()
solution()
