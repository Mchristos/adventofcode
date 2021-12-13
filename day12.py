from helpers import read_input, begin_part_one, begin_part_two, solution


def is_small(s: str):
    return s.lower() == s


def has_double_small(path):
    smalls = [vertex for vertex in path if is_small(vertex)]
    return len(set(smalls)) != len(smalls)


def get_end(edge, start):
    if start not in edge:
        raise Exception(f"start {start} not in edge {edge}")
    return list(filter(lambda x: x != start, edge))[0]


def is_valid(edge: list[str], path: list[str]):
    if path[-1] not in edge:
        return False
    end = get_end(edge, path[-1])
    if end == "start":
        return False
    if is_small(end) and end in path and has_double_small(path):
        return False
    return True


def expand_path(path: list[str], edges: list[list[str]]):
    if path[-1] == "end":
        return [path]
    valid_edges = [edge for edge in edges if is_valid(edge, path)]
    return [path + [get_end(edge, path[-1])] for edge in valid_edges]


def expand(paths, edges):
    expanded = [expanded for path in paths for expanded in expand_path(path, edges)]
    return expanded


inputs = read_input("./inputs/day12.txt")
edges = [edge.split("-") for edge in inputs]
# print(edges)
begin_part_one()
paths = [["start"]]
while True:
    paths = expand(paths, edges)
    if all([path[-1] == "end" for path in paths]):
        break
# for path in paths:
#     print(path)
solution(len(paths))
begin_part_two()
solution()
