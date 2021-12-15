from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np
import sys

sys.setrecursionlimit(10000)


def find_adj(i, length):
    i_vals = []
    if i > 0:
        i_vals.append(i - 1)
    if i < length - 1:
        i_vals.append(i + 1)
    return i_vals


def find_adjacent(position, shape):
    i, j = position
    i_vals = find_adj(i, shape[0])
    j_vals = find_adj(j, shape[1])
    return [[i, j_] for j_ in j_vals] + [[i_, j] for i_ in i_vals]


def compute_score(graph, path):
    score = 0
    for pos in path:
        score += graph[pos[0], pos[1]]
    return score


def expand_path(graph, path, visited):
    adjacents = find_adjacent(path[-1], graph.shape)
    new_visits = [next for next in adjacents if next not in visited]
    return [path + [next] for next in new_visits], new_visits


def compute_least_path(graph, paths, visited):
    # expand path with least score
    scores = [compute_score(graph, path) for path in paths]
    i_least_path = scores.index(min(scores))
    least_path = paths[i_least_path]
    distination = graph.shape
    if least_path[-1] == [distination[0] - 1, distination[1] - 1]:
        return least_path
    else:
        new_paths, new_visits = expand_path(graph, least_path, visited)
        return compute_least_path(
            graph,
            paths[:i_least_path] + paths[i_least_path + 1 :] + new_paths,
            visited + new_visits,
        )


input = read_input("./inputs/day15.txt")
risklevel = np.array([[int(x) for x in line] for line in input])


begin_part_one()
paths = [[[0, 0]]]
visited = [[0, 0]]
least_path = compute_least_path(risklevel, paths, visited)
print(least_path)
solution(sum([risklevel[x[0], x[1]] for x in least_path[1:]]))


begin_part_two()
solution()
