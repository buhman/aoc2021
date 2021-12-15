from functools import reduce


def parse_input():
    with open('input.txt') as f:
        text = f.read()
        for line in text.split('\n'):
            if line:
                yield [int(i) for i in line.strip()]


def adjacent(heightmap, x, y):
    """
            (x, y-1)
    (x-1, y)        (x+1, y)
            (x, y+1)
    """
    height = len(heightmap)
    width = len(heightmap[0])
    if x > 0:
        yield heightmap[y][x - 1], x - 1, y
    if x < (width - 1):
        yield heightmap[y][x + 1], x + 1, y
    if y > 0:
        yield heightmap[y - 1][x], x, y - 1
    if y < (height - 1):
        yield heightmap[y + 1][x], x, y + 1


def low_point(heightmap, x, y):
    point = heightmap[y][x]
    if all(
            point < adjacent_point
            for adjacent_point, _, _ in adjacent(heightmap, x, y)
    ):
        yield x, y


def low_points(heightmap):
    for y in range(len(heightmap)):
        for x in range(len(heightmap[0])):
            yield from low_point(heightmap, x, y)


def flood(heightmap, x, y, s):
    s.add((x, y))
    yield 1
    for adjacent_point, ax, ay in adjacent(heightmap, x, y):
        if (ax, ay) not in s and adjacent_point < 9:
            yield from flood(heightmap, ax, ay, s)
        else:
            s.add((ax, ay))


def basin_sizes(heightmap, lps):
    for x, y in lps:
        yield sum(flood(heightmap, x, y, set()))


def part1():
    heightmap = list(parse_input())
    lps = list(low_points(heightmap))
    part1 = sum(
        heightmap[y][x] + 1
        for x, y in lps
    )
    print("part1", part1)

    l = sorted(basin_sizes(heightmap, lps), reverse=True)
    print("part2", reduce(lambda x, a: x * a, l[:3]))

part1()
