import numpy as np 
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)

letters = 'abcdefghijklmnopqrstuvwxyz'


with open('2022/inputs/day12.txt', 'r') as f:
    lines = f.read().split('\n')
    print(lines)
    lines_ = []
    for i, line in enumerate(lines):
        line_ = []
        for j, char in enumerate(line):
            if char.islower():
                line_.append(letters.index(char))
            elif char == 'S':
                S = (i,j)
                print(S)
                line_.append(letters.index('a'))
            else:
                E = (i,j)
                print(E)
                line_.append(letters.index('z'))
        lines_.append(line_)
    grid = np.array(lines_)

    def legal_moves(pos):
        i, j = pos
        moves = []
        # up/down moves
        for i_ in [i-1, i + 1]:
            if i_ < 0 or i_ >= grid.shape[0]:
                continue
            diff = grid[i_, j] - grid[i,j]
            if -1 < diff < 2:
                moves.append((i_, j))
        # left/right moves
        for j_ in [j-1, j+1]:
            if j_ < 0 or j_ >= grid.shape[1]:
                continue
            diff = grid[i,j_] - grid[i,j]
            if -1 < diff < 2:
                moves.append((i,j_))
        return moves

    def expand(path):
        moves = [move for move in legal_moves(path[-1]) if move not in path]
        return [path + [move] for move in moves]

    def dist(A, B):
        return abs(A[0] - B[0]) + abs(A[1] - B[1])

    def find(pos, path_=[], visited_=set()):
        # print(pos, path, visited)
        path = path_.copy()
        path.append(pos)
        visited = visited_.copy()
        visited.add(pos)
        if pos == E:
            # print("found!", path)
            return (True, path)
        leastpath = None
        for child in legal_moves(pos):
            if child not in visited:
                found, childpath = find(child, path, visited)
                if found:
                    if not leastpath:
                        leastpath = childpath
                    leastpath = min(childpath, leastpath)
        if leastpath:
            return (True, leastpath)
        else:
            return (False, path)
        

    found, path = find(S)
    print(path)
    print(len(path) - 1)

    # paths = [[S]]
    # print(grid.shape)
    # print(grid[S],grid[E])
    # dists = [dist(path[-1], E) for path in paths]
    # min_dist = min(dists)
    # i_nearest = dists.index(min_dist)
    # while not min_dist == 0:
    #     # print(i_nearest)
    #     new_paths = expand(paths[i_nearest])
    #     new_dists = [dist(path[-1], E) for path in new_paths]
    #     if len(new_paths) > 0:
    #         paths.pop(i_nearest)
    #         dists.pop(i_nearest)
    #         paths += new_paths
    #         dists += new_dists
    #         new_min = min(new_dists) 
    #         if new_min < min_dist:
    #             i_nearest = dists.index(new_min)
    #             min_dist = new_min
    #         # print(len(paths))
    #     else:
    #         # print("can't expand", paths[i_nearest])
    #         paths.pop(i_nearest)
    #         dists.pop(i_nearest)
    #         min_dist = min(dists)
    #         i_nearest = dists.index(min_dist)
    # winner = paths[i_nearest]
    # print(winner)
    # print(len(winner) - 1)
