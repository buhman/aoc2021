from collections import namedtuple
from pprint import pprint


P = namedtuple("P", ["x", "y", "z"])


def dim(a, b):
    sign = (b - a) // abs(b - a) if b - a != 0 else 0
    i = a
    while i != b:
        yield i
        i += sign
    yield i


def enum_points(p1, p2):
    return (
        P(x, y, z)
        for x in dim(p1.x, p2.x)
        for y in dim(p1.y, p2.y)
        for z in dim(p1.z, p2.z)
    )


def in_range(*ps):
    return all(
        (    p.x >= -50 and p.x <= 50
         and p.y >= -50 and p.y <= 50
         and p.z >= -50 and p.z <= 50)
        for p in ps
    )


def parse_line(line):
    on_off, coord_s = line.split(" ")
    def _parse(s):
        axis, ps = s.split("=")
        a, b = ps.split("..")
        return axis, (int(a), int(b))
    l = map(_parse, coord_s.split(","))
    return on_off, dict(l)


def parse_input():
    with open('input.txt') as f:
        lines = f.read().strip().split("\n")
        return map(parse_line, lines)


def as_points(axis):
    for i in range(2):
        yield P(x=axis["x"][i],
                y=axis["y"][i],
                z=axis["z"][i])


def solution():
    points = list(map(lambda i: (i[0], list(as_points(i[1]))), parse_input()))

    cube_grid = set()

    for on_off, p1_p2 in points:
        if in_range(*p1_p2):
            for pi in enum_points(*p1_p2):
                if on_off == "on":
                    cube_grid.add(pi)
                elif on_off == "off":
                    cube_grid.discard(pi)
                else:
                    raise ValueError(on_off)
    print("part1", len(cube_grid))

    """
    cube_grid = set()
    i = 0
    for on_off, p1_p2 in points:
        print(i, len(points))
        i += 1
        for pi in enum_points(*p1_p2):
            if on_off == "on":
                cube_grid.add(pi)
            elif on_off == "off":
                cube_grid.discard(pi)
            else:
                raise ValueError(on_off)
    print("part2", len(cube_grid))
    """

solution()
