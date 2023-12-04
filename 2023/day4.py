with open("inputs/day4.txt") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    line = line.strip("\n")
    left, right = line.split(" | ")
    left = left.split(": ")[-1]
    left = left.replace("  ", " ")
    right = right.replace("  ", " ").replace("  ", " ")
    winning = [int(x) for x in left.split(" ") if x != ""]
    hand = [int(x) for x in right.split(" ") if x != ""]
    matches = 0
    for num in hand:
        if num in winning:
            matches += 1
    score = 2 ** (matches-1) if matches > 0 else 0
    # print(line, "$$", score)
    print(matches, "matches")
    sum += score

print(sum)