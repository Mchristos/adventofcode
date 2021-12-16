from helpers import read_input, begin_part_one, begin_part_two, solution
from functools import reduce

import numpy as np


def mad_multiplier(array, axis, times=5, loop=9):
    """
    Creates multiple copies of an array, stacked along the given
    axis (axis = 0 stacks new copies below, axis=1 stacks them to the right).
    Each is a copy of the original array plus one at each entry, where after
    <loop> (default 9) you loop back to 1.

    axis : 0 or 1. If 0, multiplies the array "downwards" i.e. along the 0 direction.
           If 1, multiplies to the right.
    times: Number of array copies in the result
    loop : Value after which numbers loop back to 1

    Returns a new array with dimensions [array.shape[0]*times, array.shape[1]] if axis = 0.

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


def find_adj(i, length):
    i_vals = []
    if i > 0:
        i_vals.append(i - 1)
    if i < length - 1:
        i_vals.append(i + 1)
    return i_vals


def find_adjacent(position: tuple[int], shape: tuple[int]) -> list[tuple[int]]:
    i, j = position
    i_vals = find_adj(i, shape[0])
    j_vals = find_adj(j, shape[1])
    return [(i, j_) for j_ in j_vals] + [(i_, j) for i_ in i_vals]


def compute_score(graph, path):
    score = 0
    for pos in path:
        score += graph[pos[0], pos[1]]
    return score


def expand_path(
    graph: np.ndarray, path: list[tuple[int]], score: int, visited: dict[tuple, bool]
):
    adjacents = find_adjacent(path[-1], graph.shape)
    new_visits = [next for next in adjacents if next not in visited]
    new_paths = [path + [next] for next in new_visits]
    new_scores = [score + graph[next] for next in new_visits]
    return new_paths, new_scores


def print_path(path, shape):
    picture = np.zeros(shape)
    for pos in path:
        picture[tuple(pos)] = 1
    print(picture)


def solve(graph):
    paths = [[(0, 0)]]
    scores = [0]
    visited = {(0, 0): True}
    destination = (graph.shape[0] - 1, graph.shape[1] - 1)
    while True:
        # # expand the least score path
        # scores = [compute_score(graph, path) for path in paths]
        i_least_path = scores.index(min(scores))
        new_paths, new_scores = expand_path(
            graph, paths[i_least_path], scores[i_least_path], visited
        )
        # check for solution found
        for path, score in zip(new_paths, new_scores):
            visited[path[-1]] = True
            if path[-1] == destination:
                return path, score
        # if not expand the set of paths and visits
        paths = paths[:i_least_path] + paths[i_least_path + 1 :] + new_paths
        scores = scores[:i_least_path] + scores[i_least_path + 1 :] + new_scores


input = read_input("./inputs/day15.txt")
graph = np.array([[int(x) for x in line] for line in input])


begin_part_one()
least_path, score = solve(graph)
print_path(least_path, graph.shape)
solution(score)


begin_part_two()
meta_dims = [5, 5]
graph = mad_multiplier(mad_multiplier(graph, axis=0), axis=1)
least_path, score = solve(graph)
print_path(least_path, graph.shape)
solution(score)
