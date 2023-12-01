with open("inputs/day1.txt", "r") as f:
    lines = f.readlines()

def isint(x):
    try:
        int(x)
        return True
    except:
        return False

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_last_word_idx(word, line):
    i = line.index(word)
    new_line = line[:i] + line[i + len(word):]
    if word in new_line:
        return len(word) + get_last_word_idx(word, new_line)
    else:
        return i
    


def get_first(line):
    first = None
    k = None
    for i, c in enumerate(line):
        if isint(c):
            first = c
            k = i
            break
    for d, dig in enumerate(digits):
        if dig in line:
            j = line.index(dig)
            if k is None or j < k:
                k = j
                first = str(d + 1)
    assert first is not None
    return first

def get_last(line):
    last = None
    k = None
    for i, c in enumerate(reversed(line)):
        if isint(c):
            last = c
            k = i
            break
    if k is not None:
        k = len(line) - 1 - k

    for d, dig in enumerate(digits):
        if dig in line:
            j = get_last_word_idx(dig, line)
            if k is None or j > k:
                k = j
                last = str(d + 1)
    assert last is not None
    return last 


sum = 0

for line in lines:
    first = get_first(line)
    last = get_last(line)
    # print(line, first, last)
    digit = int(first + last)
    sum += digit

print(sum)

