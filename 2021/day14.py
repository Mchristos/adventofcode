from helpers import read_input, begin_part_one, begin_part_two, solution


def count_occurrences(string: str, char: str):
    return len([char_ for char_ in string if char_ == char])


def get_character_counts(polymer: str):
    unique_chars = set(list(polymer))
    return {char: count_occurrences(polymer, char) for char in unique_chars}


inputs = read_input("./inputs/day14.txt")
polymer = inputs[0]
rules = [rule.split(" -> ") for rule in inputs[2:]]


begin_part_one()
print(polymer)
for i in range(15):
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
    print(get_character_counts(newpolymer))
    polymer = newpolymer

unique_chars = set(list(polymer))
char_counts = [count_occurrences(polymer, char) for char in unique_chars]
solution(max(char_counts) - min(char_counts))


begin_part_two()
solution()
