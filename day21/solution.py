from itertools import chain
from itertools import cycle
from collections import defaultdict


def parse_line(line):
    player_position = line.split("Player ")[1]
    player, position = player_position.split(" starting position: ")
    return int(player), int(position)


def parse_input():
    with open("input.txt") as f:
        lines = f.read().strip().split("\n")
        return map(parse_line, lines)


rolls = None


def deterministic_dice():
    global rolls
    rolls = 0
    it = iter(cycle(range(1, 100 + 1)))
    while True:
        rolls += 1
        yield next(it)



next_player = lambda player: 2 if player == 1 else 1


def move(position, spaces):
    assert position >= 1 and position <= 10
    while spaces > 0:
        position += 1
        if position > 10:
            position = 1
        spaces -= 1
    return position


def turn(player, board, dice):
    spaces = sum(map(lambda _: next(dice), range(3)))
    board[player] = move(board[player], spaces)
    return next_player(player), board, dice


def solution():
    board = dict(parse_input())
    score = defaultdict(int)
    player = 1
    dice = iter(deterministic_dice())

    while True:
        next_player, board, dice = turn(player, board, dice)
        score[player] += board[player]
        if score[player] >= 1000:
            break
        player = next_player
    global rolls
    print("part1", score[next_player] * rolls)





solution()
