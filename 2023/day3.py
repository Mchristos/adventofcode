import re 

with open("inputs/day3.txt") as f:
    lines = f.readlines()

def is_sym(x): return x != "." and not x.isdigit()

def has_sym(s):
    for c in s:
        if is_sym(c): return True
    return False

def has_adjacent(lines, i, range):
    k, l = range
    # extend range to include diags
    if -1 < (k - 1):
        k = k -1
        # check left
        if is_sym(lines[i][k]): return True
    if l + 1 < len(lines[0]):
        l = l + 1
        # check right 
        if is_sym(lines[i][l-1]): return True
    # check prev line
    if -1 < (i - 1) and has_sym(lines[i-1][k:l]):
        return True
    # check next line
    if (i + 1) < len(lines) and has_sym(lines[i+1][k:l]):
        return True
    return False

sum = 0
for i, line in enumerate(lines):
    line = line.strip("\n")
    nums = list(sorted(re.findall(r'\b\d{1,5}\b', line)))
    # if len(set(nums)) != len(nums):
    #     print(nums)
    lastnum = "xxx"
    for num in nums:
        idx = line.index(num)
        if num == lastnum:
            print(num)
            idx = (line[:idx] + line[idx + len(num): ]).index(num) + len(num)
        if has_adjacent(lines, i, (idx, idx + len(num))):
            sum += int(num)
        lastnum = num

print()
print(sum)