
# intrinsic value of a r/p/s play 
shape_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

# scores for win/lose/draw situations
play_scores = {
    # they play rock
    ('A','X') : 3,
    ('A','Y') : 6,
    ('A','Z') : 0,
    # they play paper 
    ('B','X') : 0,
    ('B','Y') : 3,
    ('B','Z') : 6,
    # they play scissors 
    ('C','X') : 6,
    ('C','Y') : 0,
    ('C','Z') : 3,
}

# Part 2
# map to what value you play given the new interpretation 
# of X/Y/Z
play_vals = {
    # they play rock
    ('A','X') : 'Z',
    ('A','Y') : 'X',
    ('A','Z') : 'Y',
    # they play paper 
    ('B','X') : 'X',
    ('B','Y') : 'Y',
    ('B','Z') : 'Z',
    # they play scissors 
    ('C','X') : 'Y',
    ('C','Y') : 'Z',
    ('C','Z') : 'X',
}

# lose / draw / win scores under the new interpretation
win_scores = {
    'X': 0,
    'Y': 3,
    'Z': 6
}




with open('inputs/day2.txt', 'r') as f:
    data = f.read()
    plays = [x.split(' ') for x in data.split('\n')]
    print("part 1")
    scores = [ shape_scores[play[1]] + play_scores[tuple(play)] for play in plays]
    # print(scores)
    print("sum =", sum(scores))

    print('\npart 2')   
    scores = [ shape_scores[play_vals[tuple(play)]] + win_scores[play[1]]  for play in plays]
    # print(scores)
    print("sum =", sum(scores))