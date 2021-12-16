from helpers import read_input, begin_part_one, begin_part_two, solution
from functools import reduce

import numpy as np


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


def print_path(path, shape):
    picture = np.zeros(shape)
    for pos in path:
        picture[tuple(pos)] = 1
    print(picture)


def mad_multiplier(array, axis, times=5, loop=9):
    """
    Creates multiple copies of an array, stacked along the given
    axis (axis = 0 stacks new copies below, axis=1 stacks them to the right).
    Each is a copy of the original array plus one at each entry, where after
    9 (loop) you loop back to 1.

    e.g. if array = [[1,2]
                     [3,4]]
    Then applying axis=0, times=3 and loop=5 yields
         [[1,2]
          [3,4]
          [2,3]
          [4,5]
          [3,4]
          [5,1]]
    """
    return reduce(
        lambda x, i: (np.concatenate((x, ((array - 1 + i) % loop) + 1), axis=axis)),
        range(1, times),
        array,
    )


input = read_input("./inputs/day15.txt")
graph = np.array([[int(x) for x in line] for line in input])


begin_part_one()
paths = [[[0, 0]]]
visited = [[0, 0]]
distination = [graph.shape[0] - 1, graph.shape[1] - 1]
while True:
    # expand path with least score
    scores = [compute_score(graph, path) for path in paths]
    i_least_path = scores.index(min(scores))
    least_path = paths[i_least_path]
    if least_path[-1] == distination:
        break
    else:
        new_paths, new_visits = expand_path(graph, least_path, visited)
        paths = paths[:i_least_path] + paths[i_least_path + 1 :] + new_paths
        visited += new_visits

print_path(least_path, graph.shape)
solution(compute_score(graph, least_path[1:]))


# begin_part_two()
# meta_dims = [5,5]
# graph = mad_multiplier(mad_multiplier(graph, axis=0), axis=1)
# paths = [[[0, 0]]]
# visited = [[0, 0]]
# distination = [graph.shape[0] - 1, graph.shape[1] - 1]
# while True:
#     # expand path with least score
#     scores = [compute_score(graph, path) for path in paths]
#     i_least_path = scores.index(min(scores))
#     least_path = paths[i_least_path]
#     if least_path[-1] == distination:
#         break
#     else:
#         new_paths, new_visits = expand_path(graph, least_path, visited)
#         paths = paths[:i_least_path] + paths[i_least_path + 1 :] + new_paths
#         visited += new_visits
# print_path(least_path, graph.shape)
# solution(compute_score(graph, least_path[1:]))
