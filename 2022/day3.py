letters = 'abcdefghijklmnopqrstuvwxyz'
letters = letters + letters.upper()

def priority(letter):
  return letters.index(letter) + 1

assert priority('a') == 1
assert priority('z') == 26

with open('inputs/day3.txt', 'r') as f:
  inputs = f.read().split('\n')

  sum = 0
  for x in inputs:
    cut = len(x)//2
    c1, c2 = x[:cut], x[cut:]
    intersect = set(c1).intersection(set(c2))
    letter = list(intersect)[0]
    sum += priority(letter)
  print("part 1")
  print(sum)

  print("\npart 2")
  sum = 0
  for i in range(len(inputs)//3):
    s1,s2,s3 = [set(x) for x in inputs[3*i : 3*i + 3]]
    # print(s1, s2, s3)
    intersect = s1.intersection(s2).intersection(s3)
    letter = list(intersect)[0]
    sum += priority(letter)
  print(sum)


