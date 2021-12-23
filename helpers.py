def begin_part_one():
    print("--- Part One ---")


def begin_part_two():
    print("--- Part Two ---")


def solution(value=""):
    print(f"Solution: {value}")


def read_input(path: str, splitlines=True) -> list[str]:
    with open(path, "r") as file:
        return file.read().split("\n") if splitlines else file.read()


def find_adj(i: int, length: int):
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
