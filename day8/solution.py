from collections import defaultdict
from itertools import combinations

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

assert len(digit_segments[8]) == 7

inverse_segments = defaultdict(set)
for k, v in digit_segments.items():
    for vi in v:
        inverse_segments[vi].add(k)
inverse_segments = dict(inverse_segments.items())


unique_digit_segments = {
    # segment count: number
    2: 1,
    4: 4,
    3: 7,
    7: 8
}


def parse_input():
    with open("sample.txt") as f:
        lines = f.read().split("\n")
    for line in lines:
        if not line:
            continue

        signal_patterns, output_value = [

            [set(digit) for digit in part.split(' ')]
            for part in line.split(' | ')
        ]
        yield signal_patterns, output_value


def infer_pattern(signal_patterns):
    possible_segment_map = dict()

    known_numbers = dict()

    for pattern in signal_patterns:
        if len(pattern) in unique_digit_segments:
            number = unique_digit_segments[len(pattern)]
            known_numbers[number] = pattern
            for segment in pattern:
                possible_segment_map[segment] = digit_segments[number].copy()
    from pprint import pprint
    #pprint(possible_segment_map)

    q = (known_numbers[7] - known_numbers[1])
    for segment, segment_set in possible_segment_map.items():
        if {segment} == q:
            segment_set = {Q}
        else:
            if Q in segment_set:
                segment_set.remove(Q)
        possible_segment_map[segment] = segment_set

    sv = (known_numbers[7] & known_numbers[1])
    for segment, segment_set in possible_segment_map.items():
        if segment not in sv:
            possible_segment_map[segment] = segment_set - {'S', 'V'}

    def combination(rest, segs, agg):
        if rest == []:
            yield agg
        else:
            k, v = rest[0]
            for seg in v:
                segs1 = segs.copy()
                try:
                    segs1.remove(seg)
                except KeyError:
                    return
                yield from combination(rest[1:], segs1, agg + [(k, seg)])


    segs = {Q, R, S, T, U, V, W}
    rest = list(sorted(possible_segment_map.items(), key=lambda t: len(t[1]), reverse=True))
    mapping = list(combination(rest, segs, []))
    assert len(mapping) == 1, mapping
    return dict(mapping[0])


def infer_pattern2(signal_patterns):
    def inner_combinations():
        for digit, segments in digit_segments.items():
            yield digit, combinations({Q, R, S, T, U, V, W}, len(segments))

    def outer_combinations(rest, agg):
        if rest == []:
            yield agg
            return
        print(rest[0])
        for digit, combinations in rest[0]:
            for combination in combinations:
                yield from outer_combinations(rest[1:], agg + [(digit, combination)])

    ic = list(inner_combinations())
    from pprint import pprint
    l = list(outer_combinations(ic, []))
    pprint(l)

def decode(pattern, lit_segments):
    translated = set(pattern[s] for s in lit_segments)
    assert len(digit_segments[8]) == 7
    for number, segments in digit_segments.items():
        print(number, sorted(segments), sorted(translated))
        if segments == translated:
            return number
    raise ValueError(lit_segments, translated)


def solution():
    digits = 0
    for signal_patterns, output_value in parse_input():
        digits += sum(1 for digit in output_value if len(digit) in unique_digit_segments)
    print("part1", digits)

    for signal_patterns, output_value in parse_input():
        pattern = infer_pattern2(signal_patterns)
        break
        pattern = infer_pattern(signal_patterns)
        print(len(set(pattern.values())))
        for lit_segments in output_value:
            print(len(lit_segments))
            print(decode(pattern, lit_segments))
        break

solution()
