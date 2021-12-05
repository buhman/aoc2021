from collections import defaultdict


def build_boards(board_lines):
    boards = []
    board = []
    for line in board_lines:
        if not line:
            if board != []:
                boards.append(board)
                board = []
            continue

        row = [int(i) for i in line.split()]
        assert row != []
        board.append(row)

    return boards


def board_lookup(board):
    for row_ix, row in enumerate(board):
        for col_ix, col in enumerate(row):
            yield col, (row_ix, col_ix)


def build_lut(boards):
    board_lut = defaultdict(list)

    for board_ix, board in enumerate(boards):
        for value, row_col in board_lookup(board):
            board_lut[value].append((board_ix, row_col))

    return board_lut


def iterate_row(board, row_ix):
    return board[row_ix]


def iterate_col(board, col_ix):
    for row in board:
        yield row[col_ix]


with open('input.txt') as f:
    input = f.read()

lines = input.split('\n')
chosen = [int(i) for i in lines[0].split(',')]
boards = build_boards(lines[1:])
board_lut = build_lut(boards)

from pprint import pprint


def bingo(drawn, board, row_ix, col_ix):

    return (
        all(n in drawn for n in iterate_row(board, row_ix))
        or all(n in drawn for n in iterate_col(board, col_ix))
    )


import copy


def part1():
    def select_winning_board(first):
        bingos = set()
        drawn = set()
        last_num = None
        last_winner = None
        last_drawn = None
        for num in chosen:
            drawn.add(num)
            for board_ix, row_col in board_lut[num]:
                if board_ix not in bingos and bingo(drawn, boards[board_ix], *row_col):
                    bingos.add(board_ix)
                    if first:
                        return num, board_ix, drawn
                    else:
                        last_num = num
                        last_winner = board_ix
                        last_drawn = copy.copy(drawn)
        if last_winner is None:
            raise ValueError("no bingo")
        else:
            return last_num, last_winner, last_drawn

    def score(winning_num, board_ix, drawn1):
        winning_board = boards[board_ix]
        unmarked = [col for row in winning_board for col in row if col not in drawn1]
        return sum(unmarked) * winning_num

    print("part1", score(*select_winning_board(True)))
    print("part2", score(*select_winning_board(False)))

part1()
