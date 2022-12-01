from helpers import read_input, begin_part_one, begin_part_two, solution
from functools import reduce

hexchar_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def hex_to_bin(hexstring: str):
    """
    Converts each hex character to a 4-digit binary string.
    Return the full (concatenated) binary string.
    e.g. "60556F" ->  011000000101010101101111
    """
    return reduce(lambda x, y: x + hexchar_to_bin[y], hexstring, "")


with open("./inputs/day16.txt") as f:
    input = f.read()

hex_values = []
while input:
    hex_values.append(input[:6])
    input = input[6:]
print(hex_values)

bin_values = [hex_to_bin(hex_) for hex_ in hex_values]
for binary in bin_values:
    print(binary)


begin_part_one()
solution()
begin_part_two()
solution()
