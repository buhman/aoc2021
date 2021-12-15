from collections import namedtuple
from pprint import pprint


Fold = namedtuple('Fold', ['axis', 'value'])
Dot = namedtuple('Dot', ['x', 'y'])


def parse_input():
    with open('input.txt') as f:
        lines = f.read().split('\n')
    for line in lines:
        if not line:
            continue
        elif line[0] == 'f':
            axis, value = line[11:].split('=')
            yield Fold(axis, int(value))
        else:
            x, y = map(int, line.split(','))
            yield Dot(x, y)


def interpret_dot(field, dot):
    point = (dot.x, dot.y)
    field.add(point)
    return point


fold_dot_axis = {
    'x': lambda point: point[0],
    'y': lambda point: point[1],
}

fold_dot_new_dot = {
    'x': lambda a, point: (a, point[1]),
    'y': lambda a, point: (point[0], a),
}


def next_max_xy(max_xy, point):
    if point[0] > max_xy[0]:
        max_xy = (point[0], max_xy[1])
    if point[1] > max_xy[1]:
        max_xy = (max_xy[0], point[1])
    return max_xy


def interpret_fold(field, fold):
    new_field = set()
    max_xy = (0, 0)
    point_axis = fold_dot_axis[fold.axis]
    new_point = fold_dot_new_dot[fold.axis]
    for point in field:
        if point_axis(point) > fold.value:
            a = (fold.value * 2) - point_axis(point)
            point = new_point(a, point)
            max_xy = next_max_xy(max_xy, point)
            new_field.add(point)
        if point_axis(point) < fold.value:
            new_field.add(point)

    #print_field(new_field, max_xy)
    return new_field, max_xy


def interpret(field, instructions, maximum_folds):
    max_xy = (0, 0)
    folds = 0
    for instruction in instructions:
        if type(instruction) == Fold:
            if folds >= maximum_folds:
                break
            print('fold', instruction)
            field, max_xy = interpret_fold(field, instruction)
            folds += 1
        elif type(instruction) == Dot:
            point = interpret_dot(field, instruction)
            max_xy = next_max_xy(max_xy, point)

        else:
            raise TypeError(type(instruction))
    return field, max_xy


def print_field(field, max_xy):
    for y in range(max_xy[1] + 1):
        for x in range(max_xy[0] + 1):
            if (x, y) in field:
                print('█', end='')
            else:
                print(' ', end='')
        print('')


def main():
    instructions = list(parse_input())
    field = set()
    field, max_xy = interpret(field, instructions, 1)

    #print_field(field, max_xy)
    print("part1", len(field))

    field = set()
    field, max_xy = interpret(field, instructions, 9999)
    print_field(field, max_xy)


main()
