from collections import defaultdict
from pprint import pprint


def parse_input():
    template = None
    rules = {}
    with open('sample.txt') as f:
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


def count(it):
    occurance = defaultdict(int)
    for i in it:
        occurance[i] += 1
    return occurance


def count2(pairs):
    counts = defaultdict(int)
    for pair, count in pairs.items():
        for element in pair:
            counts[element] += count
    return counts


def solution():
    template, rules = parse_input()
    print(template)
    step = pair_count(template)
    pprint(count2(step))
    pprint(count2(pair_count('NBCCNBBBCBHCB')))
    for _ in range(10):
        step = polymerize(step, rules)
    return

    #occurance = count(step)
    #least, *rest, most = sorted(occurance.items(), key=lambda k_v: k_v[1])
    print("part1", most[1] - least[1])

    for i in range(30):
        print(10 + i)
        step = polymerize(step, rules)
    occurance = count(step)
    least, *rest, most = sorted(occurance.items(), key=lambda k_v: k_v[1])
    print("part2", most[1] - least[1])


solution()
