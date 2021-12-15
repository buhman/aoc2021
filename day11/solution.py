from pprint import pprint


def parse_input():
    with open('input.txt') as f:
        for line in f.read().split('\n'):
            if line:
                yield [int(i) for i in line]


def adjacent(board, y, x):
    max_y = (len(board) - 1)
    max_x = (len(board[0]) - 1)

    if y > 0:
        yield (y - 1, x)
    if y < max_y:
        yield (y + 1, x)
    if x > 0:
        yield (y, x - 1)
    if x < max_x:
        yield (y, x + 1)
    """
    (>0,>0) | | (<l, >0)
    --------------------
            | |
    --------------------
    (>0,<l) | | (<l, <l)
    """
    if y > 0 and x > 0:
        yield (y - 1, x - 1)
    if y > 0 and x < max_x:
        yield (y - 1, x + 1)
    if y < max_y and x > 0:
        yield (y + 1, x - 1)
    if y < max_y and x < max_x:
        yield (y + 1, x + 1)


def propagate_flash(board, y, x, flashed):
    assert (y, x) not in flashed or board[y][x] <= 9
    if board[y][x] > 9 and (y, x) not in flashed:
        flashed.add((y, x))
        board[y][x] = 0
        for y_a, x_a in adjacent(board, y, x):
            if (y_a, x_a) not in flashed:
                board[y_a][x_a] += 1
                propagate_flash(board, y_a, x_a, flashed)


def simulate_step(board):
    flashed = set()

    for y in range(len(board)):
        for x in range(len(board[0])):
            if (y, x) not in flashed:
                board[y][x] += 1
                propagate_flash(board, y, x, flashed)

    return flashed


def solution():
    board = list(parse_input())
    flash_count = 0

    for _ in range(100):
        flashed = simulate_step(board)
        flash_count += len(flashed)

    print("part1", flash_count)


    board = list(parse_input())
    board_size = len(board) * len(board[0])
    step = 0
    while True:
        step += 1
        flashed = simulate_step(board)
        if len(flashed) == board_size:
            print("part2", step)
            break


solution()
