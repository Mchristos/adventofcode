with open("2022/inputs/day8.txt", "r") as f:
    lines = f.read().split('\n')
    grid = [ [int(x) for x in list(line)] for line in lines]
    h = len(grid)
    w = len(grid[0])
    count = 0 
    for i in range(h):
        for j in range(w):
            # print(i,j)
            if i == 0 or i == (h-1) or j == 0 or j == (w-1):
                count += 1
                continue
            # visible above
            if all([grid[y][j] < grid[i][j] for y in range(i+1, h)]):
                # print(f"visible top")
                count += 1
                continue
            # visible below
            if all([grid[y][j] < grid[i][j] for y in range(i)]):
                # print(f"visible bottom")
                count += 1
                continue
            # visible left
            if all([grid[i][x] < grid[i][j] for x in range(j)]):
                # print(f"visible left")
                count += 1
                continue
            # visible right
            if all([grid[i][x] < grid[i][j] for x in range(j+1,w)]):
                # print(f"visible left")
                count += 1
                continue
    print("part 1")
    print(count)

    highest = 0
    for i in range(h):
        for j in range(w):
            print()
            # look up
            up = 0
            y = i + 1
            while y < h:
                if grid[y][j] >= grid[i][j]:
                    up += 1
                    break
                else:
                    up += 1
                    y += 1

            # look down
            down = 0
            y = i - 1
            while y >= 0:
                if grid[y][j] >= grid[i][j]:
                    down += 1
                    break
                else:
                    down += 1
                    y -= 1

            # look right
            if (i,j) == (3,2):
                pass
            right = 0
            x = j + 1
            while x < w:
                if grid[i][x] >= grid[i][j]:
                    right += 1
                    break
                else:
                    right += 1
                    x += 1

            # look left
            left = 0
            x = j - 1
            while x >= 0:
                if grid[i][x] >= grid[i][j]:
                    left += 1
                    break
                else:
                    left += 1
                    x -= 1

            print(i,j)
            print(up, down, left, right)
            score = up * down * left * right
            print(score)
            if score > highest:
                highest = score
    print("\npart 2")
    print(highest)
            

            
