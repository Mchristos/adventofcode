from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np


def process_input(inputs: list[str]):
    digits, outputs = zip(*[line.split(" | ") for line in inputs])
    return ([x.split(" ") for x in digits], [x.split(" ") for x in outputs])


def get_signature(digit):
    """
    Returns a binary "signature" array for a digit in the form
    [a, b, c, d, e, f, g] where each value is a 1 if the digit
    contains that letter.
    Result has length 7
    """
    return np.array([1 if letter in digit else 0 for letter in "abcdefg"], dtype=int)


def decode(digits):
    """
    For 10 unknown representations of the 10 digits of a digit display,
    find which value represents which digit i, and store its signature
    in the ith position.

    E.g. if the digit 1 is represented by the string "ef" then
    result[1] = [0,0,0,0,1,1]
    i.e. the positions for a, b, c, and d are zero, and e and f are 1
    """
    # 10 digits, each with a signature of length 7
    decoded = np.zeros([10, 7], dtype=int)
    # First decode the known digits 1, 4, 7, and 8
    for digit in digits:
        if len(digit) in unique_segments:
            signature = get_signature(digit)
            if len(digit) == 2:
                decoded[1] = signature
            if len(digit) == 4:
                decoded[4] = signature
            if len(digit) == 3:
                decoded[7] = signature
            if len(digit) == 7:
                decoded[8] = signature
    # Decode 2, 3 and 5
    for digit in digits:
        if len(digit) == 5:
            signature = get_signature(digit)
            # 3 is the only digit that shares two places with 1
            if np.sum(signature * decoded[1]) == 2:
                decoded[3] = signature
            # Now its either 2 or 5. Distinguish them by how many places
            # they share with 4
            else:
                # Digit 2 shares 2 places with 4
                if np.sum(signature * decoded[4]) == 2:
                    decoded[2] = signature
                # Digit 5 shares 3 places with digit 4
                if np.sum(signature * decoded[4]) == 3:
                    decoded[5] = signature
    # Decode remaining 0, 6, 9
    for digit in digits:
        if len(digit) == 6:
            signature = get_signature(digit)
            # if you share 2 places with 7, its 6
            if np.sum(signature * decoded[7]) == 2:
                decoded[6] = signature
            # Either 0 or 9
            else:
                # 9 shares all 3's places
                if np.sum(signature * decoded[3]) == 5:
                    decoded[9] = signature
                else:
                    decoded[0] = signature
    return decoded


inputs = read_input("./inputs/day8.txt")
alldigits, alloutputs = process_input(inputs)
begin_part_one()
# 1 -> 2
# 7 -> 3
# 4 -> 4
# 8 -> 7
unique_segments = [2, 4, 3, 7]
count = 0
for outputs in alloutputs:
    for value in outputs:
        if len(value) in unique_segments:
            count += 1
solution(count)
begin_part_two()
final = 0
for (digits, outputs) in zip(alldigits, alloutputs):
    decoded = decode(digits)
    number = ""
    for output in outputs:
        signature = get_signature(output)
        for (i, row) in enumerate(decoded):
            if (signature == row).all():
                number += str(i)
    final += int(number)

solution(final)
