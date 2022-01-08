from pprint import pprint


def parse_input():
    with open("input.txt") as f:
        algorithm_s, image_s = f.read().strip().split("\n\n")

    algorithm = [
        1 if bit == "#" else 0
        for bit in algorithm_s
        if bit in {"#", "."}
    ]

    rows = image_s.split("\n")

    image = {
        (col_ix, row_ix): 1 if col == "#" else 0
        for row_ix, row in enumerate(rows)
        for col_ix, col in enumerate(row)
    }

    min_y = 0
    min_x = 0
    max_y = len(rows) - 1
    max_x = len(rows[0]) - 1

    bound = (min_x, min_y, max_y, max_y)

    return algorithm, image, bound


def print_image(image, bounds, background):
    assert background == 0

    min_x, min_y, max_x, max_y = bounds
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            c = "#" if image.get((x, y), background) else "."
            print(c, end="")
        print()


def window_coordinates(x, y):
    yield x - 1, y - 1
    yield x + 0, y - 1
    yield x + 1, y - 1

    yield x - 1, y + 0
    yield x + 0, y + 0
    yield x + 1, y + 0

    yield x - 1, y + 1
    yield x + 0, y + 1
    yield x + 1, y + 1


def window_value(image, x, y, background):
    number = 0
    for xi, yi in window_coordinates(x, y):
        pixel = image.get((xi, yi), background)
        number <<= 1
        number += pixel
    return number


def enhance(algorithm, image, bound, background):
    min_x, min_y, max_x, max_y = bound
    min_x -= 1
    min_y -= 1
    max_x += 1
    max_y += 1

    image = {
        (x, y): algorithm[window_value(image, x, y, background)]
        for x in range(min_x, max_x + 1)
        for y in range(min_y, max_y + 1)
    }
    bound = (min_x, min_y, max_y, max_y)
    return image, bound


def enhance_background(algorithm, background):
    if background == 0:
        return algorithm[0]
    if background == 1:
        return algorithm[511]


def solution():
    algorithm, image, bound = parse_input()

    background = 0

    for _ in range(2):
        image, bound = enhance(algorithm, image, bound, background)
        background = enhance_background(algorithm, background)

    assert background == 0
    print("part1", sum(image.values()))

    for _ in range(48):
        image, bound = enhance(algorithm, image, bound, background)
        background = enhance_background(algorithm, background)

    assert background == 0
    print("part2", sum(image.values()))
    print_image(image, bound, background)
    return image, bound


image, bound = solution()

with open('asdf.pbm', 'w') as f:
    f.write("P1\n")
    min_x, min_y, max_x, max_y = bound

    width = (max_x - min_x) + 1
    height = (max_y - min_y) + 1
    f.write(f"{width} {height}\n")

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            c = "1" if image.get((x, y), 0) else "0"
            print(c, end=" ", file=f)
        print(file=f)
