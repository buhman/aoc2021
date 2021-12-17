from collections import defaultdict
from pprint import pprint


def parse_input():
    template = None
    rules = {}
    with open('input.txt') as f:
        lines = f.read().split('\n')
    for line in lines:
        if not line:
            continue
        elif '-' in line:
            pair, insert = line.split(' -> ')
            rules[tuple(pair)] = insert
        else:
            template = line
    return template, rules


def polymerize(pairs, rules):
    next_pairs = defaultdict(int)
    for pair, count in pairs.items():
        if pair in rules:
            insert = rules[pair]
            next_pairs[(pair[0], insert)] += count
            next_pairs[(insert, pair[1])] += count
        else:
            next_pairs[pair] += count

    return next_pairs


def pair_count(template):
    pairs = defaultdict(int)
    for i in range(1, len(template)):
        pair = (template[i - 1], template[i])
        pairs[pair] += 1
    return pairs


def count(pairs):
    counts = defaultdict(int)
    for pair, count in pairs.items():
        counts[pair[0]] += count
    counts['B'] += 1
    return counts


def solution():
    template, rules = parse_input()
    step = pair_count(template)
    for _ in range(10):
        step = polymerize(step, rules)

    occurance = count(step)
    least, *rest, most = sorted(occurance.items(), key=lambda k_v: k_v[1])
    print("part1", most[1] - least[1])

    for i in range(30):
        step = polymerize(step, rules)
    occurance = count(step)
    least, *rest, most = sorted(occurance.items(), key=lambda k_v: k_v[1])
    print("part2", most[1] - least[1])


solution()
