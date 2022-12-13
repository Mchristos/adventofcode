with open("2022/inputs/day11_.txt", "r") as f:
    inputs = f.read().split('\n\n')
    monkeys = []
    operations = []
    actions = []

    for input in inputs:
        lines = input.split('\n')
        worries = [int(x) for x in lines[1].split('items: ')[1].split(', ')]
        monkeys.append(worries)
        operation = lines[2].split('new = ')[-1]
        mulvals = operation.split(' * ') 
        if len(mulvals) > 1:
            print(mulvals)
            if mulvals[1] == "old":
                op = lambda x: x*x
            else:
                mulval = int(mulvals[1])
                op = lambda x: x*mulval
        addvals = operation.split(' + ')
        if len(addvals) > 1:
            if addvals[1] == "old":
                op = lambda x: x + x
            else:
                addval = int(addvals[1])
                op = lambda x: x + addval
        operations.append(op)

            
        divbynum = int(lines[3].split('divisible by ')[-1])
        actions.append((divbynum, int(lines[4][-1]), int(lines[5][-1])))

    print(monkeys)
    for i_round in range(1):
        # monkeys_copy = monkeys.copy()
        for j in range(len(monkeys)):
            worries, op, action = monkeys[j], operations[j], actions[j]
            for item in worries:
                transformed = op(item)//3
                print("from", item, "to", op(item))
                if transformed % action[0] == 0:
                    print("divisible by ", action[0])
                    nextmonkey = action[1]
                else:
                    print("not divisible by ", action[0])
                    nextmonkey = action[2]
                monkeys[nextmonkey].append(transformed)
                print(monkeys)
            monkeys[j] = []
    print(monkeys)
