import re 

with open("inputs/day2.txt") as f:
    lines = f.readlines()

cols = ["red", "green", "blue"]
def col_regex(col): return re.compile(f"[0-9]+ {col}")

def get_colval(s, col):
    matches = col_regex(col).findall(s)
    if matches:
        return int(matches[0].split(" ")[0])
    else:
        return 0

#12 red cubes, 13 green cubes, and 14 blue
totals = {
    "red": 12,
    "green": 13,
    "blue": 14
}
invalids = []
valids = set()
powersum = 0
for line in lines:
    game, data = line.split(": ")
    game = int(game.split("Game ")[-1])
    maxes = [0, 0, 0]
    sets = data.split("; ")
    counts = [{col: get_colval(set_, col) for col in cols} for set_ in sets]
    for count in counts:
        for i, col in enumerate(cols):
            maxes[i] = max(maxes[i], count[col])
            if count[col] > totals[col]:
                invalids.append(game)
    power = maxes[0]*maxes[1]*maxes[2]
    powersum += power
    if game not in invalids:
        valids.add(game)
print("part 1")
print(sum(valids) , "\n")
print("part 2")
print(powersum)