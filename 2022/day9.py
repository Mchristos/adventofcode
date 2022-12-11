import numpy as np 

def move(pos: np.array, direction):
    if direction == "U":
        return pos + [0, 1]
    if direction == "D":
        return pos + [0,-1]
    if direction == "R":
        return pos + [1,0]
    if direction == "L":
        return pos + [-1,0]

def move_tail(h, t):
    diff = h - t
    if abs(diff[0]) > 1 or abs(diff[1]) > 1:
        # straight move
        if diff[0] == 0 or diff[1] == 0:
            movevec = diff/abs(diff.sum())
        # diagonal move
        elif abs(diff[0]) == 2 and abs(diff[1]) == 2:
            movevec = [diff[0]/2, diff[1]/2]
        elif abs(diff[0]) == 2:
            movevec = [diff[0]/2, diff[1]]
        elif abs(diff[1]) == 2:
            movevec = [diff[0], diff[1]/2]
        else:
            raise Exception(f"invalid diff: {diff}")
        # print("moving t by", movevec)
        return t + movevec
    return t


with open("2022/inputs/day9.txt", "r") as f:
    lines = f.read().split('\n')
    
    h = np.array([0.,0.])
    t = np.array([0.,0.])
    visited = set([tuple(t)])
    for line in lines:
        direction, number = line.split(' ')
        number = int(number)
        # print((direction, number))
        for i in range(number):
            # print("moving h with", direction)
            h = move(h, direction)
            t = move_tail(h, t)
            visited.add(tuple(t))
    print("part 1")
    print(len(visited))
    
    chain = [np.array([0.,0.]) for i in range(10)]
    visited = set([tuple(chain[-1])])
    for line in lines:
        direction, number = line.split(' ')
        number = int(number)
        # print((direction, number))
        for i in range(number):
            # print("moving h with", direction)
            chain[0] = move(chain[0], direction)
            for i in range(1,10):
                # print(i-1, i)
                # print(chain[i-1], chain[i])
                chain[i] = move_tail(chain[i-1], chain[i])
                # print(chain[i-1], chain[i])
            visited.add(tuple(chain[-1]))
    print("\npart 2")
    print(len(visited))


                

                