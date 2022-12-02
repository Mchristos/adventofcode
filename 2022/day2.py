# rps = rock, paper, scissors
rps_map = {
    'X': 'r',
    'Y': 'p',
    'Z': 's',
    'A': 'r',
    'B': 'p',
    'C': 's'
}

# off by one from the points to work well with modular arithmetic
rps_val = {
    'r': 0,
    'p': 1,
    's': 2
}

# paper vs rock     1 - 0 =      1 (mod 3) => WIN 
# rock vs paper     0 - 1 = -1 = 2 (mod 3) => LOSE
# scissors vs paper 2 - 1 =      1 (mod 3) => WIN
# rock vs scissors  0 - 2 =      1 (mod 3) => WIN
# rock vs rock      0 - 0 =      0 (mod 3) => TIE 
def score(them, me):
    assert them in 'rps'
    assert me in 'rps'
    diff = (rps_val[me] - rps_val[them]) % 3 
    # 0 (mod 3) is a tie, e.g. 2 - 2
    if diff == 0:
        return 3
    # 1 (mod 3) is a win 
    if diff == 1:
        return 6
    # 2 (mod 3) is a lose, e.g. 3 - 1 = 2
    if diff == 2:
        return 0


with open('inputs/day2.txt', 'r') as f:
    data = f.read()
    plays = [x.split(' ') for x in data.split('\n')]
    print("part 1")
    scores = []
    for play in plays:
        them, me = [rps_map[p] for p in play]
        scores.append(score(them, me) + rps_val[me] + 1)
    print("sum =", sum(scores))

    print('\npart 2')
    scores = []
    for play in plays:
        them = rps_map[play[0]]
        xyz = play[1]
        # lose
        if xyz == 'X':
            score_ = 0
            value = (rps_val[them] - 1) % 3 + 1
        # draw
        if xyz == 'Y':
            score_ = 3
            value = rps_val[them] + 1
        # win
        if xyz == 'Z':
            score_ = 6
            value = (rps_val[them] + 1) % 3 + 1
        scores.append(score_ + value)

    print("sum =", sum(scores))