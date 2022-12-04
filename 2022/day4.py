with open("inputs/day4.txt", 'r') as f:
  data = f.read().split('\n')

  count = 0
  count2 = 0
  for x in data:
    elfs = [tuple(int(z) for z in y.split('-')) for y in x.split(',')]
    elf1, elf2 = elfs
    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
      count += 1
    elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
      count += 1

    range1, range2 = (set(range(elf[0], elf[1] + 1)) for elf in elfs)
    if range1.intersection(range2):
      count2 += 1
  print(count)
  print(count2)


  # ranges = [[tuple(int(z) for z in y.split('-')) for y in x.split(',')] for x in data]
  # print(ranges)