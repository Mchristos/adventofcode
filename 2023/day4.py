with open("inputs/day4.txt") as f:
    lines = f.readlines()

def p1_score(matches):
    return 2 ** (matches-1) if matches > 0 else 0

def get_matches(winning, hand):
    matches = 0
    for num in hand:
        if num in winning:
            matches += 1
    return matches

def get_leftright(line):
    line = line.strip("\n")
    left, right = line.split(" | ")
    left = left.split(": ")[-1]
    left = left.replace("  ", " ")
    right = right.replace("  ", " ").replace("  ", " ")
    return left, right

p1 = 0
copies = [1] * len(lines)
for i, line in enumerate(lines):
    left, right = get_leftright(line)
    winning = [int(x) for x in left.split(" ") if x != ""]
    hand = [int(x) for x in right.split(" ") if x != ""]
    matches = get_matches(winning, hand)
    # for each copy of the card
    for _ in range(copies[i]):
        # add the associated copies from matches
        for j in range(matches):
            copies[i + 1 + j] += 1
    p1 += p1_score(matches)

print("part 1:", p1)
print("part 2:", sum(copies))