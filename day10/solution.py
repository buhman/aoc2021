from functools import reduce


def parse_input():
    with open("input.txt") as f:
        lines = f.read().split("\n")
    return lines


delimiters = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">",
}


points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


complete_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def find_first_error(line):
    stack = []

    for character in line:
        if character in set(["}", ")", "]", ">"]):
            delim = stack.pop()
            if delimiters[delim] != character:
                return False, (delimiters[delim], character)
            else:
                pass
        elif character in set(["{", "(", "[", "<"]):
            stack.append(character)
        else:
            raise ValueError(repr(line), repr(character))

    return True, stack


def part1(lines):
    for line in lines:
        ok, ret = find_first_error(line)
        if not ok:
            expected, found = ret
            yield points[found]


def score_stack(stack):
    next_score = lambda s, c: s * 5 + complete_points[delimiters[c]]
    return reduce(next_score, reversed(stack), 0)


def part2(lines):
    for line in lines:
        if not line:
            continue
        ok, ret = find_first_error(line)
        if not ok:
            continue
        stack = ret
        yield score_stack(stack)



def solution():
    lines = parse_input()
    print("part1", sum(part1(lines)))
    scores = sorted(part2(lines))
    print("part2", scores[len(scores) // 2])

solution()
