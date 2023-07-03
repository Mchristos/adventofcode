import numpy as np 

with open('2022/inputs/day14_.txt','r') as f:
    lines = f.read().split('\n')
    xmin = np.inf
    xmax = -np.inf
    ymin = np.inf
    ymax = -np.inf
    data = []
    for line in lines:
        coords = np.array([[int(y) for y in x.split(',')] for x in line.split(' -> ')])
        data.append(coords)
        for coord in coords:
            xmin = min(xmin, coord[0])
            xmax = max(xmax, coord[0])
            ymax = max(ymax, coord[1])
    print(xmin, ymin)
    grid = np.zeros([xmax - xmin + 1, ymax + 1])
    print(grid.shape)
    for seq in data:
        for i in range(1, len(seq)):
            diff = seq[i] - seq[i-1]
            start = seq[i-1] - np.array([xmin, 0])
            print(seq[i-1], start, diff)
            if diff[0] == 0:
                print("vertical")
                grid[start[0], start[1] : (start[1] + diff[1])] = 111
            else:
                print("horizontal")
                grid[start[0] : (start[0] + diff[0]) , start[1]] = 111
            print(grid)
    print(grid)

