with open("2022/inputs/day8.txt", "r") as f:
    lines = f.read().split('\n')
    grid = [ [int(x) for x in list(line)] for line in lines]
    h = len(grid)
    w = len(grid[0])
    count = 0 
    for i in range(h):
        for j in range(w):
            print(i,j)
            if i == 0 or i == (h-1) or j == 0 or j == (w-1):
                count += 1
                continue
            # visible above
            if all([grid[y][j] < grid[i][j] for y in range(i+1, h)]):
                print(f"visible top")
                count += 1
                continue
            # visible below
            if all([grid[y][j] < grid[i][j] for y in range(i)]):
                print(f"visible bottom")
                count += 1
                continue
            # visible left
            if all([grid[i][x] < grid[i][j] for x in range(j)]):
                print(f"visible left")
                count += 1
                continue
            # visible right
            if all([grid[i][x] < grid[i][j] for x in range(j+1,w)]):
                print(f"visible left")
                count += 1
                continue
    print("part 1")
    print(count)

            
