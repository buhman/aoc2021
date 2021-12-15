from collections import defaultdict
from pprint import pprint


def parse_input():
    with open('input.txt') as f:
        lines = f.read().split('\n')
    for line in lines:
        if line:
            start, end = line.split('-')
            yield start, end


def build_adjacencies(paths):
    adj = defaultdict(set)
    for a, b in paths:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def all_paths(node, adjacencies, seen, path):
    if node == 'end':
        yield path + [node]
        return

    seen = seen.copy()
    seen.add(node)

    assert node in adjacencies
    for adj in adjacencies[node]:
        if adj.upper() == adj or adj not in seen:
            yield from all_paths(adj, adjacencies, seen, path + [node])


def all_paths2(node, adjacencies, seen, path, small):
    if node == 'end':
        yield path + [node]
        return

    seen = seen.copy()
    seen[node] += 1

    assert node in adjacencies
    for adj in adjacencies[node]:
        if adj == 'start':
            continue

        if adj.upper() == adj or adj not in seen:
            yield from all_paths2(adj, adjacencies, seen, path + [node], small)
        elif adj in seen and not small:
            yield from all_paths2(adj, adjacencies, seen, path + [node], True)


def solution():
    paths = list(parse_input())
    adjacencies = build_adjacencies(paths)
    paths = list(all_paths('start', adjacencies, set(), []))
    print('part1', len(paths))

    paths = list(all_paths2('start', adjacencies, defaultdict(int), [], False))
    print('part2', len(paths))


solution()
