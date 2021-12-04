from helpers import read_input, begin_part_one, begin_part_two, solution
import numpy as np


def process_input(input: list[str]) -> tuple[list[int], list[np.ndarray]]:
    numbers = [int(value) for value in input[0].split(",")]
    boards: list[np.ndarray] = []
    board = []
    for (i, row) in enumerate(input[2:]):
        if row == "":
            np_board = np.array(board)
            if np_board.shape != (5, 5):
                raise Exception(f"invalid board {np_board}")
            boards.append(np_board)
            board = []
        else:
            board.append([int(value) for value in row.split(" ") if value != ""])
            # handle final row
            if i == len(input) - 3:
                boards.append(np.array(board))
    return (numbers, boards)


def is_winning(marked_board: np.ndarray):
    column_sums = marked_board.sum(axis=0)
    row_sums = marked_board.sum(axis=1)
    rows, cols = marked_board.shape
    return np.any(column_sums == rows) or np.any(row_sums == cols)


def compute_score(board, marked_board, winning_number):
    unmarked_sum = 0
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if marked_board[i, j] == 0:
                unmarked_sum += board[i, j]
    return unmarked_sum * winning_number


def solve_part2(numbers, boards):
    marked_boards = [np.zeros((5, 5)) for i in range(len(boards))]
    winning = np.zeros(len(boards))
    lasttowin_index = -1
    for number in numbers:
        # mark each board with the position of the number
        for (i, board) in enumerate(boards):
            marked_boards[i] += board == number
            # check if board wins
            if is_winning(marked_boards[i]):
                winning[i] = 1
                if i == lasttowin_index:
                    score = compute_score(board, marked_boards[i], number)
                    return score
                if winning.sum() == len(boards) - 1:
                    lasttowin_index = np.where(winning == 0)[0][0]


input = read_input("./inputs/day4.txt")
numbers, boards = process_input(input)

begin_part_one()
begin_part_two()
score = solve_part2(numbers, boards)
solution(score)
solution()
