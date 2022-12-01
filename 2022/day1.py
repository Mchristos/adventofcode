
with open("inputs/day1.txt", "r") as f:
    inputs = f.read().split("\n\n")
    elves = [sum([int(x) for x in elf.split('\n')]) for elf in inputs]
    print("part 1")
    print(max(elves))

    print("\npart 2")
    top3 = sorted(elves)[-3:]
    print(top3)
    print("sum =", sum(top3))