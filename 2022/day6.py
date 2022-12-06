with open('inputs/day6.txt', 'r') as f:
    input = f.read()
    print("part 1")
    for i in range(len(input) - 4):
        if len(set(input[i:i+4])) == 4:
            print(i + 4)
            break
    print("\npart 2")
    for i in range(len(input) - 14):
        if len(set(input[i:i+14])) == 14:
            print(i + 14)
            break
