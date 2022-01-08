def parse_input():
    with open('input.txt') as f:
        blob = f.read()

    lines = blob.split('\n')
    for line in lines:
        if not line:
            continue
        direction, magnitude = line.split(' ')
        yield direction, int(magnitude)


def part1():
    horizontal_axis = 0
    depth_axis = 0

    for direction, magnitude in parse_input():
        if direction == "up":
            depth_axis = depth_axis - magnitude
        elif direction == "down":
            depth_axis = depth_axis + magnitude
        elif direction == "forward":
            horizontal_axis = horizontal_axis + magnitude

    print("depth", depth_axis)
    print("horizontal", horizontal_axis)
    print("part1 answer", depth_axis * horizontal_axis)


def part2():
    aim = 0
    horizontal_axis = 0
    depth_axis = 0

    for direction, magnitude in parse_input():
        if direction == "up":
            aim -= magnitude
        elif direction == "down":
            aim += magnitude
        elif direction == "forward":
            horizontal_axis += magnitude
            depth_axis += aim * magnitude

    print("depth", depth_axis)
    print("horizontal", horizontal_axis)
    print("part1 answer", depth_axis * horizontal_axis)

part1()
part2()
