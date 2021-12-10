from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np

OPENING = ["[", "{", "(", "<"]

CLOSING = ["]", "}", ")", ">"]

CORRUPTED_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}

COMPLETION_SCORES = {"(": 1, "[": 2, "{": 3, "<": 4}

lines = read_input("./inputs/day10.txt")
corrupted_chars = []
completion_scores = []
for line in lines:
    opens = []
    corrupted = None
    for char in line:
        if char in OPENING:
            opens.append(char)
        if char in CLOSING:
            # valid closing character
            if len(opens) > 0 and CLOSING.index(char) == OPENING.index(opens[-1]):
                opens.pop()
            else:
                corrupted = char
                break
    if corrupted:
        corrupted_chars.append(corrupted)
    else:
        # we have an incomplete line
        completion_score = 0
        for char in reversed(opens):
            completion_score = 5 * completion_score + COMPLETION_SCORES[char]
        completion_scores.append(completion_score)


begin_part_one()
solution(sum([CORRUPTED_SCORES[char] for char in corrupted_chars]))

begin_part_two()
solution(int(np.median(completion_scores)))
