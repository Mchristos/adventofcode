with open('inputs/day5.txt', 'r') as f:
    lines = f.read().split('\n')
    stacks_index = lines.index('') - 1
    stacks = [list() for x in lines[stacks_index].split(' '*3)]

    for line in reversed(lines[:stacks_index]):
        vals = [line[i:i+4] for i in range(0, len(line), 4)]
        for i in range(len(vals)):
            val = vals[i].strip().strip('[').strip(']')
            if val:
                stacks[i].append(val)
    stacks_p2 = [stack.copy() for stack in stacks]

    moves = lines[stacks_index + 2:]
    for move in moves:
        tokens = move.split(' ')
        quantity = int(tokens[1])
        from_ = int(tokens[3]) - 1
        to = int(tokens[5]) - 1
        for i in range(quantity):
            stacks[to].append(stacks[from_].pop())
        stacks_p2[to] += stacks_p2[from_][-quantity:]
        stacks_p2[from_] = stacks_p2[from_][:-quantity]

    solution = ''
    solution_p2 = ''
    for i in range(len(stacks)):
        solution += stacks[i].pop()
        solution_p2 += stacks_p2[i].pop()
    print('part 1')
    print(solution)

    print('\npart 2')
    print(solution_p2)





        

    # while line != "":
    #     print(line)
    #     line = f.readline()
    
