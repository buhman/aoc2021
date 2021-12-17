from collections import defaultdict
from pprint import pprint
from itertools import combinations
from itertools import chain


"""

 qq
r  s
r  s
 tt
u  v
u  v
 ww

"""
Q, R, S, T, U, V, W = "Q", "R", "S", "T", "U", "V", "W"


digit_segments = {
    0: {Q, R, S, U, V, W},
    1: {S, V},
    2: {Q, S, T, U, W},
    3: {Q, S, T, V, W},
    4: {R, S, T, V},
    5: {Q, R, T, V, W},
    6: {Q, R, T, U, V, W},
    7: {Q, S, V},
    8: {Q, R, S, T, U, V, W},
    9: {Q, R, S, T, V, W}
}


def parse_input():
    with open("input.txt") as f:
        lines = f.read().split("\n")
    for line in lines:
        if not line:
            continue

        signal_patterns, output_value = [

            [set(digit) for digit in part.split(' ')]
            for part in line.split(' | ')
        ]
        yield signal_patterns, output_value


def match_signal_patterns(signal_patterns):
    for signal in signal_patterns:
        for digit, segments in digit_segments.items():
            if len(segments) == len(signal):
                yield digit, signal


def flatten(d: list[int, list[set]], acc):
    if d == []:
        yield acc
        return

    first, *rest = d
    digit, signals = first
    for signal in signals:
        yield from flatten(rest, [(digit, signal)] + acc)


def dict_list(l):
    d = defaultdict(list)
    for k, v in l:
        d[k].append(v)
    return list(dict(d).items())


def check_setwise(p):
    for a, b in combinations(p, 2):
        a_digit, a_segment = a
        b_digit, b_segment = b

        digit_difference = digit_segments[a_digit] ^ digit_segments[b_digit]
        digit_intersect  = digit_segments[a_digit] & digit_segments[b_digit]

        segment_difference = a_segment ^ b_segment
        segment_intersect  = a_segment & b_segment

        if len(digit_difference) == len(segment_difference) \
           and len(digit_intersect) == len(segment_intersect):
            continue
        else:
            return False
    return True


def find_digit_map(signal_pattern):
    d = dict_list(match_signal_patterns(signal_pattern))

    possible = list(filter(check_setwise, flatten(d, [])))
    assert len(possible) == 1, possible

    signal_map = {frozenset(v): k for k, v in possible[0]}
    return signal_map


def output_digits():
    for signal_pattern, output_values in parse_input():
        digit_map = find_digit_map(signal_pattern)
        yield [digit_map[frozenset(value)] for value in output_values]


def digit_list_as_int(dl):
    n = 0
    for i in dl:
        n *= 10
        n += i
    return n


def solution():
    digits = list(output_digits())
    part1_digits = {1, 4, 7, 8}
    print("part1", sum(1 for n in chain.from_iterable(digits) if n in part1_digits))

    print("part2", sum(digit_list_as_int(n) for n in digits))


solution()
