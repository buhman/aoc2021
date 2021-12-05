from collections import defaultdict
from functools import partial
from itertools import cycle, islice
from queue import deque


def parse_input():
    with open('input.txt') as f:
        text = f.read()

    def parse_point(field):
        return tuple(int(i) for i in field.split(','))

    for line in text.split('\n'):
        if not line:
            continue
        fields = line.split(' -> ')
        yield tuple(map(parse_point, fields))


X = 0
Y = 1


def axis_aligned(line):
    return (
           line[0][X] == line[1][X]
        or line[0][Y] == line[1][Y]
    )


def line_points(line):
    def points(axis):
        a0 = line[0][axis]
        a1 = line[1][axis]
        sign = a1 - a0
        sign = sign // abs(sign) if sign != 0 else sign
        while True:
            yield a0

            if a0 == a1:
                return
            a0 += sign

    def axes_points():
        for axis in [0, 1]:
            yield points(axis)

    x_points, y_points = map(list, axes_points())

    point_count = max(map(len, [x_points, y_points]))
    return islice(zip(cycle(x_points), cycle(y_points)), point_count)


def plot_line(field: dict[tuple[int, int], int],
              points: list[tuple[int, int]]):
    for point in points:
        field[point] += 1


def solution():
    lines = list(parse_input())

    for part, lines in [("part1", filter(axis_aligned, lines)),
                        ("part2", lines)]:
        field = defaultdict(int)
        deque(map(partial(plot_line, field), map(line_points, lines)),
              maxlen=0)

        answer = sum(1 for bit in field.values() if bit > 1)
        print(part, answer)


solution()
